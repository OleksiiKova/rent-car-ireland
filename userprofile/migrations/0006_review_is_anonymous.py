# Generated by Django 4.2.13 on 2024-07-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
