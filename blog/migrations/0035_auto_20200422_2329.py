# Generated by Django 2.0 on 2020-04-22 17:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0034_chords'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chords',
            new_name='Chord',
        ),
    ]