# Generated by Django 4.2 on 2023-09-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email_us',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
