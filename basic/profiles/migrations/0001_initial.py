# Generated by Django 2.2 on 2019-12-03 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='title')),
                ('domain', models.CharField(max_length=50, unique=True, verbose_name='domain')),
            ],
            options={
                'verbose_name': 'mobile provider',
                'verbose_name_plural': 'mobile providers',
                'db_table': 'user_mobile_providers',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True, verbose_name='gender')),
                ('mugshot', models.FileField(blank=True, upload_to='mugshots', verbose_name='mugshot')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('address1', models.CharField(blank=True, max_length=100, verbose_name='address1')),
                ('address2', models.CharField(blank=True, max_length=100, verbose_name='address2')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='city')),
                ('state', models.CharField(blank=True, help_text='or Province', max_length=100, verbose_name='state')),
                ('zip', models.CharField(blank=True, max_length=10, verbose_name='zip')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='country')),
                ('mobile', localflavor.us.models.PhoneNumberField(blank=True, max_length=20, verbose_name='mobile')),
                ('mobile_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.MobileProvider')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user profile',
                'verbose_name_plural': 'user profiles',
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='title')),
                ('url', models.URLField(blank=True, help_text="URL with a single '{user}' placeholder to turn a username into a service URL.", verbose_name='url')),
            ],
            options={
                'verbose_name': 'service type',
                'verbose_name_plural': 'service types',
                'db_table': 'user_service_types',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Username or id to be inserted into the service url.', max_length=100, verbose_name='Name or ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.ServiceType')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'db_table': 'user_services',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('url', models.URLField(verbose_name='url')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
                'db_table': 'user_links',
            },
        ),
    ]
