# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 05:28
from __future__ import unicode_literals

import cloudstorage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudstorage', '0002_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='location',
            new_name='folder',
        ),
        migrations.AddField(
            model_name='file',
            name='original_name',
            field=models.CharField(default='Boop', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=cloudstorage.models.get_file_path),
        ),
    ]
