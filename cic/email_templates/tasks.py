from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.utils.html import strip_tags

from cic.Lead.models import Lead
from cic.Master.models import DelayedEvent
from cic.users.models import User
from config.email_backend import dynamic_send_email

from .models import EmailTemplate


@shared_task(bind=True)
def send_welcome_email(self, to: list, user_id: int):
    email_template = EmailTemplate.objects.get(name="Welcome Email")

    user_obj = User.objects.get(id=user_id)

    dynamic_send_email(
        subject=email_template.subject,
        body=email_template.body,
        to=to,
        user=user_obj,
        attachments=email_template.attachments,
    )


@shared_task(bind=True)
def send_product_questionaire_email(self, lead_id: int):
    """This sends emails of all the products that are in a lead.

    Args:
        to (list): list of emails that will receive the email
        user_id (int): id of the Lead Id.
    """

    lead = Lead.objects.get(id=lead_id)
    assiged_user = lead.assigned_to
    _to = [lead.primary_email, lead.secondary_email]
    to = [i for i in _to if i]
    email_templates = EmailTemplate.objects.filter(product__in=lead.products.all())

    for email_template in email_templates:
        dynamic_send_email(
            subject=email_template.subject,
            body=email_template.body,
            to=to,
            user=assiged_user,
            attachments=email_template.attachments,
        )


def send_email_user_reminder_after_quotation():
    delayed_events = DelayedEvent.objects.filter(
        is_processed=False,
        event_type="user_reminder",
        due_date__lte=timezone.now(),
    )
    if delayed_events.count() > 0:
        for event in delayed_events:
            email_data = event.data["email_data"]
            html_content = email_data["body"]
            plain_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject=email_data["subject"],
                body=plain_content,
                to=[email_data["to"]],
            )

            email.attach_alternative(html_content, "text/html")
            if email.send(fail_silently=False):
                event.is_processed = True
                event.save(update_fields=["is_processed"])


def send_client_reminders():
    events = DelayedEvent.objects.filter(
        due_date__lte=timezone.now(),
        event_type="client_reminder",
        is_processed=False,
    )
    if events.count() > 0:
        for event in events:
            if dynamic_send_email(
                **event.data.get("email_data", {}),
                config=event.data.get("config", {}),
            ):
                event.is_processed = True
                event.save(update_fields=["is_processed"])


@shared_task(bind=True)
def process_delayed_events(self):
    send_client_reminders()
    send_email_user_reminder_after_quotation()
