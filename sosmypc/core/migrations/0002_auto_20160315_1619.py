# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualificacaoprofissoespessoa',
            name='profissaopessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualificacaoProfissoesPessoa', to='core.ProfissoesPessoa'),
        ),
    ]
