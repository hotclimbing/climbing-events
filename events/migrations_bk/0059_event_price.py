# Generated by Django 4.0.4 on 2022-10-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0058_alter_event_yoomoney_wallet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
