# Generated by Django 5.0.8 on 2024-08-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lead', '0003_alter_lead_first_name_followuptask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
