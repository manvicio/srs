# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='imagen',
            field=models.ImageField(default=1, upload_to=b'team', blank=True),
            preserve_default=False,
        ),
    ]
