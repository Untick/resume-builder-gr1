# Generated by Django 4.2.4 on 2023-09-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("do_order", "0002_ordercl_ordercv_created_time_ordercv_edited_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordercv",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="ordercv",
            name="edited_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
