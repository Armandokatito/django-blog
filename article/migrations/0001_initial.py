# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 05:37
from __future__ import unicode_literals

import article.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('body', models.TextField()),
                ('pub_date', models.TimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('thumbnail', models.FileField(upload_to=article.models.get_upload_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
        ),
    ]
