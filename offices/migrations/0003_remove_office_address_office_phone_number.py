# Generated by Django 4.2.13 on 2024-07-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0002_remove_office_google_map_link_office_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='address',
        ),
        migrations.AddField(
            model_name='office',
            name='phone_number',
            field=models.CharField(default=3532221117, help_text='Office phone number', max_length=20),
            preserve_default=False,
        ),
    ]
