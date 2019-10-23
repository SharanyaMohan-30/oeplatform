# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 07:19
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modelview", "0016_auto_20160302_0805")]

    operations = [
        migrations.AlterField(
            model_name="basicfactsheet",
            name="authors",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="Who are the authors? Where do / did they work, on which parts of the model, during which time period?",
                    max_length=300,
                ),
                default=list,
                null=True,
                size=None,
                verbose_name="Author(s) (institution, working field, active time period) (comma-separated)",
            ),
        )
    ]
