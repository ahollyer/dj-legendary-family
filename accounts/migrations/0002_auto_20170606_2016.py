# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default='Add a quick status update or bio here!', max_length=800),
        ),
    ]