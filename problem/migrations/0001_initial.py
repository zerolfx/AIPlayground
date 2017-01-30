# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 13:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='#')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('submissions', models.IntegerField(default=0, verbose_name='Submissions')),
                ('status', models.CharField(choices=[('r', 'Removed'), ('a', 'Available')], max_length=1, verbose_name='Status')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Likes')),
                ('time_limit', models.IntegerField(default=1000, verbose_name='Time Limit (ms)')),
                ('memory_limit', models.IntegerField(default=512, verbose_name='Memory Limit (MB)')),
                ('program_limit', models.IntegerField(default=128, verbose_name='Program Limit (KB)')),
                ('combat_type', models.IntegerField(choices=[(1, 'Single'), (2, 'Combat')], default=1, verbose_name='Combat Type')),
                ('description', models.TextField(verbose_name='Description')),
                ('input', models.TextField(verbose_name='Input')),
                ('output', models.TextField(verbose_name='Output')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.FileField(upload_to='', verbose_name='Input')),
                ('output', models.FileField(upload_to='', verbose_name='Output')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='samples',
            field=models.ManyToManyField(to='problem.Sample'),
        ),
    ]
