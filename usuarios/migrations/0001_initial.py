# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microposts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('pseudonimo', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('correo', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('foto', models.ImageField(upload_to=b'')),
                ('posts', models.ManyToManyField(to='microposts.Post')),
                ('seguidores', models.ManyToManyField(to='usuarios.Usuario', through='usuarios.Relaciones')),
            ],
        ),
        migrations.AddField(
            model_name='relaciones',
            name='seguidor',
            field=models.ForeignKey(related_name='seguidor', to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='relaciones',
            name='sigue',
            field=models.ForeignKey(related_name='sigue', to='usuarios.Usuario'),
        ),
    ]
