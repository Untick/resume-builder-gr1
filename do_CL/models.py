from django.db import models

from do_order.models import OrderCL
from users.models import Registration


class DoCL(models.Model):
    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    order_id = models.ForeignKey(OrderCL, on_delete=models.CASCADE)
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
