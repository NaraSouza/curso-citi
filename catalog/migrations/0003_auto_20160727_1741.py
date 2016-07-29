# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160727_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_approved',
            field=models.BooleanField(default=True, verbose_name='Aprovado'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Preço'),
        ),
    ]