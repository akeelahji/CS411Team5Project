# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchText', models.CharField(max_length=200)),
            ],
        ),
    ]
