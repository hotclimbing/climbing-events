# Generated by Django 3.1.3 on 2021-10-14 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0042_auto_20211013_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='last_calc_results_time',
        ),
    ]
