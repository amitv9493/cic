from django.conf import settings
from django.db import models

from cic.Master.models import Client_Type
from cic.Master.models import Industry_Type as Lead_Industry
from cic.Master.models import Lead_Source
from cic.Master.models import Lead_Status
from cic.Master.models import lead_Followup_Status
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

    lead_source = models.ForeignKey(Lead_Source, on_delete=models.CASCADE)
    lead_status = models.ForeignKey(Lead_Status, on_delete=models.CASCADE)
    lead_Industry = models.ForeignKey(Lead_Industry, on_delete=models.CASCADE)
    client_type = models.ForeignKey(Client_Type, on_delete=models.CASCADE)
    lead_followup_status = models.ForeignKey(
        lead_Followup_Status, on_delete=models.CASCADE
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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
