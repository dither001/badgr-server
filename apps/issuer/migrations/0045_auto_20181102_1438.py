# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-02 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0044_auto_20180713_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgeclass',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='badgeinstance',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='issuer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
