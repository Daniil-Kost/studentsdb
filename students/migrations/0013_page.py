# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-23 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_exam_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name of Page')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('url_field', models.CharField(max_length=256, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='HTML content')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Page',
            },
        ),
    ]