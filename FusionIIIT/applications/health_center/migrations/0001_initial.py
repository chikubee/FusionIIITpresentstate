# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 10:33
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
            name='Ambulance_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('approval', models.NullBooleanField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=100, null=True)),
                ('complaint', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_phone', models.CharField(max_length=10)),
                ('specialization', models.CharField(choices=[('0', 'Cardiology'), ('1', 'Oncology'), ('2', 'Gynaecology'), ('3', 'Radiology'), ('4', 'General Practitioner'), ('5', 'Primary Care Physician'), ('6', 'Opthomology'), ('7', 'Dental')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Health_Card',
            fields=[
                ('health_card', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_admit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_doctor', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=50)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(max_length=50)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescribed_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=100, null=True)),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('test', models.CharField(blank=True, max_length=200, null=True)),
                ('test_file', models.FileField(blank=True, null=True, upload_to='Administrator/health_center/')),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Appointment')),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('room', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('threshold', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stockinventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Stock')),
            ],
        ),
        migrations.AddField(
            model_name='prescribed_medicine',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Stock'),
        ),
        migrations.AddField(
            model_name='prescribed_medicine',
            name='prescription_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Prescription'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Stock'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Schedule'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo'),
        ),
    ]
