# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180515_1546'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='goods2',
            new_name='goods',
        ),
    ]
