# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 17:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectedAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('facebook', 'Facebook')], max_length=255, verbose_name='Service')),
                ('identifier', models.CharField(db_index=True, max_length=255, verbose_name='Service Identifier')),
                ('service_token', models.TextField(blank=True, verbose_name='Service Token')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_accounts', to=settings.AUTH_USER_MODEL, verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Connected Account',
                'verbose_name_plural': 'Connected Accounts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='connectedaccount',
            unique_together=set([('service', 'identifier')]),
        ),
    ]