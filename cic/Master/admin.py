from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Client_Type
from .models import DelayedEvent
from .models import EmailTemplateCategory
from .models import Industry_Type
from .models import Lead_Source
from .models import Lead_Status
from .models import Product_Category
from .models import lead_Followup_Status


# Define resources for import/export
class LeadSourceResource(resources.ModelResource):
    class Meta:
        model = Lead_Source


class IndustryTypeResource(resources.ModelResource):
    class Meta:
        model = Industry_Type


class LeadStatusResource(resources.ModelResource):
    class Meta:
        model = Lead_Status


class ClientTypeResource(resources.ModelResource):
    class Meta:
        model = Client_Type


class LeadFollowupStatusResource(resources.ModelResource):
    class Meta:
        model = lead_Followup_Status


class ProductCategoryResource(resources.ModelResource):
    class Meta:
        model = Product_Category


# Define admin classes with search and filter capabilities
@admin.register(Lead_Source)
class LeadSourceAdmin(ImportExportModelAdmin):
    resource_class = LeadSourceResource
    list_display = ("source_name",)
    search_fields = ("source_name",)
    list_filter = ("source_name",)


@admin.register(Industry_Type)
class IndustryTypeAdmin(ImportExportModelAdmin):
    resource_class = IndustryTypeResource
    list_display = ("industry_name",)
    search_fields = ("industry_name",)
    list_filter = ("industry_name",)


@admin.register(Lead_Status)
class LeadStatusAdmin(ImportExportModelAdmin):
    resource_class = LeadStatusResource
    list_display = ("status_name",)
    search_fields = ("status_name",)
    list_filter = ("status_name",)


@admin.register(Client_Type)
class ClientTypeAdmin(ImportExportModelAdmin):
    resource_class = ClientTypeResource
    list_display = ("client_type_name",)
    search_fields = ("client_type_name",)
    list_filter = ("client_type_name",)


@admin.register(lead_Followup_Status)
class LeadFollowupStatusAdmin(ImportExportModelAdmin):
    resource_class = LeadFollowupStatusResource
    list_display = ("followup_status_name",)
    search_fields = ("followup_status_name",)
    list_filter = ("followup_status_name",)


@admin.register(Product_Category)
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
