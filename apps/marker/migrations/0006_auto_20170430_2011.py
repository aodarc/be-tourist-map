# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 20:11
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0005_auto_20170430_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Місце розташування'),
        ),
    ]