# Generated by Django 5.0.8 on 2024-08-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Organisation Name')),
                ('primary_phone', models.CharField(max_length=20, verbose_name='Primary Phone')),
                ('primary_email', models.EmailField(max_length=254, verbose_name='Primary Email')),
                ('website', models.URLField(verbose_name='Website')),
                ('organization_location', models.CharField(max_length=255, verbose_name='Organisation Location')),
                ('postal_address', models.TextField(verbose_name='Postal Address for communication')),
                ('notes', models.TextField(blank=True, verbose_name='Notes/Remarks')),
            ],
        ),
    ]
