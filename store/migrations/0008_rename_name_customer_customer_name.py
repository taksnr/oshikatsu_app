# Generated by Django 4.1.3 on 2022-11-21 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_rename_first_name_customer_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer", old_name="name", new_name="customer_name",
        ),
    ]
