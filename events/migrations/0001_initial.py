# Generated by Django 4.0.4 on 2022-10-17 18:26

import colorfield.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import events.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('yoomoney_wallet_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('gym', models.CharField(max_length=128)),
                ('date', models.DateField(null=True)),
                ('poster', models.ImageField(default='../static/events/img/default_poster.png', upload_to='posters')),
                ('description', models.TextField(null=True)),
                ('short_description', models.TextField(max_length=200, null=True)),
                ('routes_num', models.IntegerField(default=10, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_registration_open', models.BooleanField(default=False)),
                ('is_results_allowed', models.BooleanField(default=False)),
                ('is_enter_result_allowed', models.BooleanField(default=False)),
                ('is_count_only_entered_results', models.BooleanField(default=False)),
                ('is_view_full_results', models.BooleanField(default=False)),
                ('is_view_route_color', models.BooleanField(default=False)),
                ('is_view_route_grade', models.BooleanField(default=False)),
                ('is_view_route_score', models.BooleanField(default=False)),
                ('is_separate_score_by_groups', models.BooleanField(default=False)),
                ('is_update_results_after_enter', models.BooleanField(default=True)),
                ('score_type', models.CharField(choices=[('SUM', 'Сумма баллов'), ('PROP', 'От кол-ва пролазов')], default='SUM', max_length=4)),
                ('flash_points', models.IntegerField(default=100)),
                ('redpoint_points', models.IntegerField(default=80)),
                ('group_num', models.IntegerField(default=1)),
                ('group_list', models.CharField(default='Общая группа', max_length=200)),
                ('set_num', models.IntegerField(default=1)),
                ('set_list', models.CharField(default='Общий сет', max_length=200)),
                ('set_max_participants', models.IntegerField(default=0)),
                ('registration_fields', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('gender', 'Пол'), ('birth_year', 'Год рождения'), ('city', 'Город'), ('team', 'Команда'), ('grade', 'Разряд'), ('email', 'Email')], default='gender,birth_year,city,team', max_length=39, null=True)),
                ('required_fields', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('birth_year', 'Год рождения'), ('city', 'Город'), ('team', 'Команда'), ('email', 'Email')], default=None, max_length=26, null=True)),
                ('is_without_registration', models.BooleanField(default=False)),
                ('is_view_pin_after_registration', models.BooleanField(default=True)),
                ('is_check_result_before_enter', models.BooleanField(default=False)),
                ('is_update_result_allowed', models.BooleanField(default=True)),
                ('participant_min_age', models.IntegerField(default=0)),
                ('yoomoney_wallet_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_male', models.FloatField(default=1)),
                ('points_female', models.FloatField(default=1)),
                ('number', models.IntegerField()),
                ('grade', models.CharField(choices=[('5', '5'), ('6A', '6A'), ('6A+', '6A+'), ('6B', '6B'), ('6B+', '6B+'), ('6C', '6C'), ('6C+', '6C+'), ('7A', '7A'), ('7A+', '7A+'), ('7B', '7B'), ('7B+', '7B+'), ('7C', '7C'), ('7C+', '7C+'), ('8A', '8A'), ('8A+', '8A+'), ('8B', '8B'), ('8B+', '8B+'), ('8C', '8C'), ('8C+', '8C+')], default='5', max_length=3)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('score_json', models.JSONField(default=events.models._get_blank_json)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('MALE', 'М'), ('FEMALE', 'Ж')], default='MALE', max_length=6)),
                ('birth_year', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=32, null=True)),
                ('team', models.CharField(max_length=32, null=True)),
                ('grade', models.CharField(choices=[('BR', 'б/р'), ('3Y', '3 ю.р.'), ('2Y', '2 ю.р.'), ('1Y', '1 ю.р.'), ('3C', '3 сп.р.'), ('2C', '2 сп.р.'), ('1C', '1 сп.р.'), ('KMS', 'КМС'), ('MS', 'МС'), ('MSMK', 'МСМК')], default='BR', max_length=4)),
                ('pin', models.PositiveSmallIntegerField(null=True)),
                ('score', models.FloatField(default=0)),
                ('is_entered_result', models.BooleanField(default=False)),
                ('group_index', models.IntegerField(default=0)),
                ('set_index', models.IntegerField(default=0)),
                ('accents', models.JSONField(default=events.models._get_blank_json)),
                ('place', models.IntegerField(default=0)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='events.event')),
            ],
        ),
    ]
