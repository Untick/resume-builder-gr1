# Generated by Django 4.2.4 on 2023-08-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderCV",
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
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Мужской"), ("F", "Женский")], max_length=1
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("position_sought", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                (
                    "employment_type",
                    models.CharField(
                        choices=[
                            ("full_time", "Полная занятость"),
                            ("part_time", "Частичная занятость"),
                            ("freelance", "Фриланс"),
                            ("internship", "Стажировка"),
                        ],
                        max_length=20,
                    ),
                ),
                ("schedule", models.CharField(max_length=100)),
                (
                    "experience_level",
                    models.CharField(
                        choices=[
                            ("no_experience", "Нет опыта"),
                            ("junior", "Junior"),
                            ("mid", "Middle"),
                            ("senior", "Senior"),
                        ],
                        max_length=20,
                    ),
                ),
                ("last_job", models.CharField(max_length=255)),
                ("last_position", models.CharField(max_length=100)),
                ("tasks_at_previous_jobs", models.TextField()),
                ("about_me", models.TextField()),
                ("key_skills", models.TextField()),
                ("education_university", models.CharField(max_length=255)),
            ],
        ),
    ]
