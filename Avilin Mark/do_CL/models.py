from django.db import models

from do_order.models import OrderCL
from users.models import Registration


class DoCL(models.Model):
    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    order_id = models.ForeignKey(OrderCL, on_delete=models.CASCADE)
    letter = models.TextField()
    created_time = models.TimeField(auto_now_add=True)
    edited_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.edited_time
