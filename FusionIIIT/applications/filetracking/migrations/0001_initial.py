# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 11:03
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('subject', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='globals.ExtraInfo')),
            ],
            options={
                'db_table': 'File',
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField(auto_now_add=True)),
                ('forward_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('forward_flag', models.BooleanField(default=False)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('current_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
                ('file_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filetracking.File')),
                ('receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to='globals.ExtraInfo')),
            ],
            options={
                'db_table': 'Tracking',
            },
        ),
    ]
