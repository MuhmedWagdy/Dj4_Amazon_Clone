# Generated by Django 4.2 on 2023-10-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_cart_total_after_coupen_alter_order_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_after_coupen',
            new_name='total_after_coupon',
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='0fyfhf5f', max_length=100),
        ),
    ]
