# Generated by Django 5.0.8 on 2024-08-12 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lead', '0007_alter_lead_mobile_phone_alter_lead_primary_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followuptask',
            old_name='lead_folloup_status',
            new_name='lead_followup_status',
        ),
    ]
