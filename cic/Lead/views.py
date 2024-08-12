from datetime import timedelta

from django.utils import timezone

from cic.Lead.models import FollowupTask
from cic.Lead.models import Lead
from cic.Master.models import DelayedEvent
from cic.Master.models import LeadFollowupStatus
from cic.users.models import User


def create_client_reminder(user: User, lead_obj: Lead):
    for i in [2, 4, 8, 12]:
        DelayedEvent.objects.create(
            event_type="client_reminder",
            due_date=timezone.now() + timedelta(days=i),
            data={
                "email_data": {
                    "from": user.from_email,
                    "subject": f"client reminder after {i} secs",
                    "body": "This is a reminder for your reply.",
                    "to": [lead_obj.primary_email, lead_obj.secondary_email],
                },
                "config": {
                    "password": user.email_password,
                    "Username": user.email_username,
                    "port": user.email_port,
                    "host": user.email_host,
                },
            },
        )

        # also create followup tasks for assigned users
        FollowupTask.objects.create(
            lead=lead_obj,
            lead_followup_status=LeadFollowupStatus.objects.get(
                followup_status_name="Pending",
            ),
            due_date=timezone.now() + timedelta(days=i),
            assigned_to=user,
        )


def crete_user_reminder(lead_obj: Lead):
    for i in [10, 20, 60, 90]:
        subject = f"Reminder to contact client after sending quotation {i} seconds."
        DelayedEvent.objects.create(
            event_type="user_reminder",
            data={
                "email_data": {
                    "subject": subject,
                    "body": "<h1>Reminder</h1>",
                    "to": lead_obj.assigned_to.email,
                },
            },
            due_date=timezone.now() + timedelta(days=i),
        )
