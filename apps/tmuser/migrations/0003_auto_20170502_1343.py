# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmuser', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
