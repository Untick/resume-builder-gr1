from django.db import models

from users.models import Registration


class DoCV(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    EXPERIENCE_CHOICES = [
        ('no_experience', 'Нет опыта'),
        ('junior', 'Junior'),
        ('mid', 'Middle'),
        ('senior', 'Senior'),
    ]

    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position_sought = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=255)
    schedule = models.CharField(max_length=100)
    experience = models.TextField()
    about_me = models.TextField()
    key_skills = models.TextField()
    education_university = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='cv_image', null=True, blank=True)

    def __str__(self):
        return self.fullname
