# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 19:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_auto_20170706_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phototag',
            options={'ordering': ('user',)},
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(related_name='_photo_tags_+', through='main.PhotoTag', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='phototag',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.Photo'),
        ),
        migrations.AlterField(
            model_name='phototag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
