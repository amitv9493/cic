# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

from cic.Master.models import IndustryType

User = get_user_model()


class Organization(models.Model):
    organization_name = models.CharField(
        max_length=255,
        verbose_name="Organisation Name",
    )
    primary_phone = models.CharField(max_length=20, verbose_name="Primary Phone")
    primary_email = models.EmailField(verbose_name="Primary Email")
    website = models.URLField(verbose_name="Website")
    industry = models.ForeignKey(
        IndustryType,
        on_delete=models.CASCADE,
        verbose_name="Industry",
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Assigned to",
    )

    # New fields
    organization_location = models.CharField(
        max_length=255,
        verbose_name="Organisation Location",
    )
    postal_address = models.TextField(verbose_name="Postal Address for communication")
    notes = models.TextField(verbose_name="Notes/Remarks", blank=True)

    def __str__(self):
        return self.organization_name
