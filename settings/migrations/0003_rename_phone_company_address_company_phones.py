# Generated by Django 4.2 on 2023-09-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_company_email_us'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='phone',
            new_name='address',
        ),
        migrations.AddField(
            model_name='company',
            name='phones',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
