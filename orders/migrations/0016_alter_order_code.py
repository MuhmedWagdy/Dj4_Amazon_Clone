# Generated by Django 4.2 on 2023-10-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_rename_total_after_coupen_cart_total_after_coupon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='kdd32jt0', max_length=100),
        ),
    ]
