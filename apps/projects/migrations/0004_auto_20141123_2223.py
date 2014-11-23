# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20141123_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(upload_to=b'media', blank=True),
            preserve_default=True,
        ),
    ]
