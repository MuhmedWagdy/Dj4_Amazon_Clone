# Generated by Django 4.2 on 2023-09-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_cart_detail_cartdetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='od836k54', max_length=100),
        ),
    ]