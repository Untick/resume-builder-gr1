# Generated by Django 4.2.5 on 2023-09-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CV",
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
                ("REC_ID", models.BinaryField()),
                ("TIMESTAMP", models.DateTimeField(auto_now_add=True)),
                ("STUDENT_ID", models.TextField()),
                ("CV_ID", models.TextField()),
                ("CV_NAME", models.TextField()),
                ("CV_PATTERN", models.TextField()),
                ("TARGET_POSITION", models.TextField(blank=True)),
                ("TARGET_SALARY", models.TextField()),
                ("EMPLOYMENT_FORM", models.TextField(blank=True)),
                ("WORKPLACE", models.TextField(blank=True)),
                ("BUSINESS_TRIP", models.BooleanField(default=False)),
                ("RELOCATE", models.BooleanField(default=False)),
                ("FOREIGN_LANG", models.TextField(blank=True)),
                ("SKILLS", models.TextField(blank=True)),
                ("STRENGTHS", models.TextField(blank=True)),
                ("EXPERIENCE", models.TextField(blank=True)),
                ("EDUCATION", models.TextField(blank=True)),
                ("CERTIFICATES", models.TextField(blank=True)),
                ("PUBLICATIONS", models.TextField(blank=True)),
                ("ACHIEVEMENTS", models.TextField(blank=True)),
                ("REFERENCES", models.TextField(blank=True)),
                ("RECOMMENDATIONS", models.TextField(blank=True)),
                ("HOBBIES", models.TextField(blank=True)),
                ("ABOUT", models.TextField(blank=True)),
                ("COVER_LETTER", models.TextField(blank=True)),
            ],
        ),
    ]