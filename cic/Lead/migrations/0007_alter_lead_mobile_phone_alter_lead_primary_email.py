# Generated by Django 5.0.8 on 2024-08-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lead', '0006_alter_lead_client_type_alter_lead_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='lead',
            name='primary_email',
            field=models.EmailField(max_length=254),
        ),
    ]
