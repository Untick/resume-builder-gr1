from django.db import models


class Registration(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
