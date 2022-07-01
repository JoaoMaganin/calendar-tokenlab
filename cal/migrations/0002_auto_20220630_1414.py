# Generated by Django 3.2.13 on 2022-06-30 17:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Evento',
            new_name='Event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='fim',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='inicio',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='titulo',
            new_name='title',
        ),
    ]
