# Generated by Django 2.0 on 2020-04-17 10:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200417_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
