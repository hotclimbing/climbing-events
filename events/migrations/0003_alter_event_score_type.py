# Generated by Django 4.0.8 on 2022-11-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_is_update_results_after_enter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='score_type',
            field=models.CharField(choices=[('SUM', 'Сумма баллов'), ('PROP', 'От количества пролазов'), ('TBL', 'По таблице категорий'), ('NUM', 'По количеству Всего/Flash')], default='SUM', max_length=4),
        ),
    ]
