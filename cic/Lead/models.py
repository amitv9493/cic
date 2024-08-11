from django.conf import settings
from django.db import models

from cic.Master.models import ClientType
from cic.Master.models import IndustryType as LeadIndustry
from cic.Master.models import LeadFollowupStatus
from cic.Master.models import LeadSource
from cic.Master.models import LeadStatus
from cic.Products.models import Products


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    primary_phone = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    primary_email = models.EmailField()
    secondary_email = models.EmailField()
    company_website = models.CharField(max_length=100)
    lead_location = models.CharField(max_length=100)

    lead_source = models.ForeignKey(LeadSource, on_delete=models.CASCADE)
    lead_status = models.ForeignKey(LeadStatus, on_delete=models.CASCADE)
    lead_industry = models.ForeignKey(LeadIndustry, on_delete=models.CASCADE)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    lead_followup_status = models.ForeignKey(
        LeadFollowupStatus,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(Products, blank=True)
    notes = models.TextField()
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.lead_status}"
