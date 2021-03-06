# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-27 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0013_merge_20190127_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('speaker', models.TextField()),
                ('venue', models.TextField(max_length=200, null=True)),
                ('registration_link', models.CharField(max_length=300)),
            ],
        ),
    ]
