# -*- coding: utf-8 -*-
# Generated by Django 1.11.19 on 2019-03-04 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("login", "0017_auto_20181119_1631")]

    operations = [
        migrations.RenameField(
            model_name="myuser", old_name="mail_address", new_name="email"
        )
    ]
