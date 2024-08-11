from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ClientType
from .models import DelayedEvent
from .models import EmailTemplateCategory
from .models import IndustryType
from .models import LeadFollowupStatus
from .models import LeadSource
from .models import LeadStatus
from .models import ProductCategory


# Define resources for import/export
class LeadSourceResource(resources.ModelResource):
    class Meta:
        model = LeadSource


class IndustryTypeResource(resources.ModelResource):
    class Meta:
        model = IndustryType


class LeadStatusResource(resources.ModelResource):
    class Meta:
        model = LeadStatus


class ClientTypeResource(resources.ModelResource):
    class Meta:
        model = ClientType


class LeadFollowupStatusResource(resources.ModelResource):
    class Meta:
        model = LeadFollowupStatus


class ProductCategoryResource(resources.ModelResource):
    class Meta:
        model = ProductCategory


# Define admin classes with search and filter capabilities
@admin.register(LeadSource)
class LeadSourceAdmin(ImportExportModelAdmin):
    resource_class = LeadSourceResource
    list_display = ("source_name",)
    search_fields = ("source_name",)
    list_filter = ("source_name",)


@admin.register(IndustryType)
class IndustryTypeAdmin(ImportExportModelAdmin):
    resource_class = IndustryTypeResource
    list_display = ("industry_name",)
    search_fields = ("industry_name",)
    list_filter = ("industry_name",)


@admin.register(LeadStatus)
class LeadStatusAdmin(ImportExportModelAdmin):
    resource_class = LeadStatusResource
    list_display = ("status_name",)
    search_fields = ("status_name",)
    list_filter = ("status_name",)


@admin.register(ClientType)
class ClientTypeAdmin(ImportExportModelAdmin):
    resource_class = ClientTypeResource
    list_display = ("client_type_name",)
    search_fields = ("client_type_name",)
    list_filter = ("client_type_name",)


@admin.register(LeadFollowupStatus)
class LeadFollowupStatusAdmin(ImportExportModelAdmin):
    resource_class = LeadFollowupStatusResource
    list_display = ("followup_status_name",)
    search_fields = ("followup_status_name",)
    list_filter = ("followup_status_name",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(ImportExportModelAdmin):
    resource_class = ProductCategoryResource
    list_display = ("category_name",)
    search_fields = ("category_name",)
    list_filter = ("category_name",)


# Register models with the admin site


@admin.register(EmailTemplateCategory)
class EmailTemplateCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DelayedEvent)
class DelayedEventAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "due_date",
        "is_processed",
    )

    list_filter = ("is_processed",)
