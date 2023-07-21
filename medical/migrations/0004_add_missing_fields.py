# Generated by Django 3.2.18 on 2023-05-12 15:11

import core.fields
import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0003_mutations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='pat_cat',
            new_name='patient_category',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='pat_cat',
            new_name='patient_category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='row_id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='row_id',
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(db_column='Quantity', decimal_places=2, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='uuid',
            field=models.CharField(db_column='ItemUUID', default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='uuid',
            field=models.CharField(db_column='ServiceUUID', default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='service',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
    ]