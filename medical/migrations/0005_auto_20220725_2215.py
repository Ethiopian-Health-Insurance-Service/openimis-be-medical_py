# Generated by Django 3.0.14 on 2022-07-25 22:15

import core.fields
import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0004_auto_20220725_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='packagetype',
            field=models.CharField(db_column='ServPackageType', default='S', max_length=1),
        ),
    ]
