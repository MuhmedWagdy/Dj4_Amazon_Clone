# Generated by Django 4.2 on 2023-10-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='8u4hg5fg', max_length=100),
        ),
    ]
