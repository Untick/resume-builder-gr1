# Generated by Django 4.2.5 on 2023-09-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("REC_ID", models.TextField()),
                ("TIMESTAMP", models.DateTimeField(auto_now_add=True)),
                ("STUDENT_ID", models.TextField()),
                ("LOGIN", models.TextField(blank=True)),
                ("PWD", models.TextField(blank=True)),
                ("NAME", models.TextField(blank=True)),
                ("SURNAME", models.TextField(blank=True)),
                ("PATRONYMIC", models.TextField(blank=True)),
                ("PHOTO", models.BinaryField()),
                ("GENDER", models.BooleanField()),
                ("BIRTHDATE", models.DateTimeField()),
                ("EMAIL", models.TextField(blank=True)),
                ("PHONE", models.TextField(blank=True)),
                ("RESIDENCY", models.TextField(blank=True)),
                ("STATUS", models.BinaryField()),
            ],
        ),
    ]
