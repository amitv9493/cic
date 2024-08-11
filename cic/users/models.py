from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    email_host = models.CharField(max_length=255, null=True)
    email_port = models.IntegerField(null=True)
    email_username = models.CharField(max_length=255,null=True)
    email_password = models.CharField(max_length=255, null=True)
    email_use_tls = models.BooleanField(default=True,null=True)
    from_email = models.EmailField(null=True)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})