# Generated by Django 4.2 on 2023-09-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_cart_status_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='khhk421a', max_length=100),
        ),
    ]
