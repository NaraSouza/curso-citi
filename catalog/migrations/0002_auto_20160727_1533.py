# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
