from django.db import models


# Create your models here.
class LeadSource(models.Model):
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return self.source_name


class IndustryType(models.Model):
    industry_name = models.CharField(max_length=100)

    def __str__(self):
        return self.industry_name


class LeadStatus(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.status_name}"


class ClientType(models.Model):
    client_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.client_type_name


class LeadFollowupStatus(models.Model):
    followup_status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.followup_status_name


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class EmailTemplateCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class DelayedEvent(models.Model):
    event_type = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    data = models.JSONField(default=dict)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ("-due_date",)

    def __str__(self):
        return f"{self.event_type} due on {self.due_date}"
