# Generated by Django 4.2.5 on 2023-10-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderCL",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("job_title", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("experience", models.TextField()),
                ("skills", models.TextField()),
                ("created_time", models.TimeField(auto_now_add=True)),
                ("edited_time", models.TimeField(auto_now=True)),
            ],
        ),
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
                ("fullname", models.CharField(max_length=100)),
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
                ("employment_type", models.CharField(max_length=255)),
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("edited_time", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="cv_image"),
                ),
            ],
        ),
    ]
