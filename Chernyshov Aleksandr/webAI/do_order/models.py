from django.db import models


class OrderCV(models.Model):
    GENDER_CHOICES = [
        ("M", "Мужской"),
        ("F", "Женский"),
    ]

    EXPERIENCE_CHOICES = [
        ("no_experience", "Нет опыта"),
        ("junior", "Junior"),
        ("mid", "Middle"),
        ("senior", "Senior"),
    ]

    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position_sought = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=255)
    schedule = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    last_job = models.CharField(max_length=255)
    last_position = models.CharField(max_length=100)
    tasks_at_previous_jobs = models.TextField()
    about_me = models.TextField()
    key_skills = models.TextField()
    education_university = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="cv_image", null=True, blank=True)

    def __str__(self):
        return self.fullname


class OrderCL(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()
    created_time = models.TimeField(auto_now_add=True)
    edited_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.full_name
