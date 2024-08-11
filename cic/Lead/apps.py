from django.apps import AppConfig


class LeadConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cic.Lead"

    def ready(self) -> None:
        pass
