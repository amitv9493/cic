from typing import Any

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from cic.email_templates.tasks import send_product_questionaire_email

from .models import FollowupTask
from .models import Lead
from .views import create_client_reminder
from .views import crete_user_reminder


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
        "lead_industry",
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
        "lead_industry",
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
                    "lead_industry",
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
                if form.cleaned_data.get("lead_status").status_name == "Welcome Email Received":
                    send_product_questionaire_email.delay(lead_id=obj.id)

                    create_client_reminder(user=obj.assigned_to, lead_obj=obj)

                elif form.cleaned_data.get("lead_status").status_name == "Quotation Sent":
                    crete_user_reminder(lead_obj=obj)
        return super().save_model(request, obj, form, change)


@admin.register(FollowupTask)
class FollowupTaskAdmin(admin.ModelAdmin):
    pass
