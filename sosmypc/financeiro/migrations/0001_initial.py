# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
    ]
