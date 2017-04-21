# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steam_app', '0003_auto_20170420_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='game',
            name='id_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='steam_app.UserProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='steam_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='steam_app.UserProfile'),
        ),
        migrations.AlterField(
            model_name='clan',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='steam_app.UserProfile'),
        ),
    ]
