# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-13 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_exercise', models.CharField(max_length=15)),
                ('name_exercise', models.CharField(max_length=50)),
                ('video_exercise', models.URLField(blank=True, max_length=150, null=True)),
                ('audio_exercise', models.URLField(blank=True, max_length=150, null=True)),
                ('question', models.TextField(default='')),
                ('answers', models.TextField(default='')),
                ('true_answer', models.TextField(default='')),
                ('audio_true_answer', models.URLField(blank=True, max_length=150, null=True)),
                ('permission', models.CharField(max_length=10)),
                ('estimated_time', models.DecimalField(decimal_places=3, max_digits=10)),
                ('limited_time', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]