# Generated by Django 2.0 on 2020-04-20 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200420_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 20, 22, 40, 0, 428230)),
        ),
    ]
