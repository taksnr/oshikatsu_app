# Generated by Django 4.1.3 on 2022-11-21 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_rename_name_customer_customer_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="customer", name="customer_name",),
        migrations.AddField(
            model_name="customer",
            name="first_name",
            field=models.CharField(default=12345, max_length=20),
            preserve_default=False,
        ),
    ]
