# Generated by Django 3.1.3 on 2021-04-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0032_auto_20210417_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_without_registration',
            field=models.BooleanField(default=False),
        ),
    ]
