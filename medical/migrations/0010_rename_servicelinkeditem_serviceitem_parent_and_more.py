# Generated by Django 4.2.10 on 2024-05-22 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("medical", "0009_alter_service_patient_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="serviceitem",
            old_name="servicelinkedItem",
            new_name="parent",
        ),
        migrations.RenameField(
            model_name="serviceservice",
            old_name="servicelinkedService",
            new_name="parent",
        ),
    ]