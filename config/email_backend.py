from pathlib import Path

from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.smtp import EmailBackend
from django.utils.html import strip_tags

from cic.users.models import User


class DynamicEmailBackend(EmailBackend):
    def __init__(self, config, **kwargs):
        super().__init__(**config, **kwargs)


def dynamic_send_email(  # noqa: PLR0913
    subject: str,
    body,
    to: list,
    from_email: str | None = None,
    user: User | None = None,
    config: dict | None = None,
    **kwargs,
):
    if user:
        config = {
            "host": user.email_host,
            "port": user.email_port,
            "username": user.email_username,
            "password": user.email_password,
        }
    backend = DynamicEmailBackend(config)

    # Create plain-text content
    plain_text_content = strip_tags(body)

    # The original HTML content
    html_content = body

    email = EmailMultiAlternatives(
        subject=subject,
        body=plain_text_content,
        from_email=user.from_email if user else from_email,
        to=to,
        connection=backend,
    )

    email.attach_alternative(html_content, "text/html")
    if (attachments := kwargs.get("attachments")) and attachments.all().count() != 0:
        for attachment in attachments.all():
            file_extension = Path(attachment.file.name).suffix

            new_filename = f"{attachment.name}{file_extension}"
            email.attach(new_filename, attachment.file.read())

    return email.send(fail_silently=False)
