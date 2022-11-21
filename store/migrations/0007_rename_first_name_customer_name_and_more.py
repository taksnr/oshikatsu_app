# Generated by Django 4.1.3 on 2022-11-21 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_order_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer", old_name="first_name", new_name="name",
        ),
        migrations.RemoveField(model_name="customer", name="last_name",),
        migrations.RemoveField(model_name="customer", name="phone",),
    ]
