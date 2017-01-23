# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_auto_20170123_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={},
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='created',
        ),
    ]
