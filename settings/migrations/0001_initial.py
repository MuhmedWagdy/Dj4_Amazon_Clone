# Generated by Django 4.2 on 2023-09-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='company')),
                ('subtitle', models.TextField(max_length=100)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twiter_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, max_length=100, null=True)),
                ('email', models.TextField(blank=True, max_length=100, null=True)),
                ('android_app', models.TextField(blank=True, max_length=100, null=True)),
                ('ios_app', models.TextField(blank=True, max_length=100, null=True)),
                ('call_us', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
