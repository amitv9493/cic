from datetime import timedelta
from typing import TYPE_CHECKING
from typing import Any

from django.contrib import admin
from django.utils import timezone
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from cic.email_templates.tasks import send_product_questionaire_email
from cic.Master.models import DelayedEvent

from .models import Lead

if TYPE_CHECKING:
    from cic.users.models import User


# Define the resource for import/export
class LeadResource(resources.ModelResource):
    class Meta:
        model = Lead


# Define the admin class with search, filter, and fieldsets capabilities
@admin.register(Lead)
class LeadAdmin(ImportExportModelAdmin):
    resource_class = LeadResource
    list_display = (
        "first_name",
        "last_name",
        "company_name",
        "primary_phone",
        "primary_email",
        "lead_source",
        "lead_status",
        "lead_Industry",
        "client_type",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "company_name",
        "primary_phone",
        "primary_email",
    )
    list_filter = (
        "lead_source",
        "lead_status",
        "lead_Industry",
        "client_type",
        "created_at",
    )
    filter_horizontal = ("products",)
    ordering = ("-created_at",)

    fieldsets = (
        ("Personal Information", {"fields": ("first_name", "last_name")}),
        ("Company Information", {"fields": ("company_name", "company_website")}),
        (
            "Contact Information",
            {
                "fields": (
                    "primary_phone",
                    "mobile_phone",
                    "primary_email",
                    "secondary_email",
                ),
            },
        ),
        (
            "Lead Details",
            {
                "fields": (
                    "lead_location",
                    "lead_source",
                    "lead_status",
                    "lead_Industry",
                    "client_type",
                    "lead_followup_status",
                    "assigned_to",
                    "products",
                    "notes",
                ),
            },
        ),
        (
            "Meta Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "created_by",
                ),
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
    )

    def save_model(self, request: Any, obj: Lead, form: Any, change) -> None:
        if not change:
            obj.created_by = request.user

        if change:
            changed_fields = form.changed_data
            if "lead_status" in changed_fields:
                if (
                    form.cleaned_data.get("lead_status").status_name
                    == "Welcome Email Received"
                ):
                    send_product_questionaire_email.delay(lead_id=obj.id)
                    user: User = obj.assigned_to
                    for i in [2, 4, 8, 12]:
                        DelayedEvent.objects.create(
                            event_type="client_reminder",
                            due_date=timezone.now() + timedelta(seconds=i),
                            data={
                                "email_data": {
                                    "from": user.from_email,
                                    "subject": f"client reminder after {i} secs",
                                    "body": "This is a reminder for your reply.",
                                    "to": [obj.primary_email, obj.secondary_email],
                                },
                                "config": {
                                    "password": user.email_password,
                                    "Username": user.email_username,
                                    "port": user.email_port,
                                    "host": user.email_host,
                                },
                            },
                        )

                elif (
                    form.cleaned_data.get("lead_status").status_name == "Quotation Sent"
                ):
                    for i in [10, 20, 60, 90]:
                        subject = f"Reminder to contact client after sending quotation {i} seconds."  # noqa: E501
                        DelayedEvent.objects.create(
                            event_type="user_reminder",
                            data={
                                "email_data": {
                                    "subject": subject,
                                    "body": "<h1>Reminder</h1>",
                                    "to": obj.assigned_to.email,
                                },
                            },
                            due_date=timezone.now() + timedelta(seconds=i),
                        )
        return super().save_model(request, obj, form, change)
