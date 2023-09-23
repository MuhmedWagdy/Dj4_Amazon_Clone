# Generated by Django 4.2 on 2023-09-23 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='75f4g0g3', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
