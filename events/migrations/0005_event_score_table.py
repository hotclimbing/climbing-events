# Generated by Django 4.0.8 on 2022-11-16 09:34

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_route_score_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='score_table',
            field=models.JSONField(default=events.models._get_default_score_table_json),
        ),
    ]
