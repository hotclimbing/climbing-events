# Generated by Django 4.0.4 on 2022-10-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='yoomoney_secret_key',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
