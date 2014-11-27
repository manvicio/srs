# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TextoServices',
            new_name='TextoProyectos',
        ),
        migrations.RenameModel(
            old_name='TextoProjects',
            new_name='TextoServicios',
        ),
    ]
