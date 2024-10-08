# Generated by Django 5.0.8 on 2024-08-11 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lead', '0001_initial'),
        ('Master', '0001_initial'),
        ('Products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lead',
            name='client_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.clienttype'),
        ),
        migrations.AddField(
            model_name='lead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_followup_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.leadfollowupstatus'),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.industrytype'),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.leadsource'),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.leadstatus'),
        ),
        migrations.AddField(
            model_name='lead',
            name='products',
            field=models.ManyToManyField(blank=True, to='Products.products'),
        ),
    ]
