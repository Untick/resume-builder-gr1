from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class WebsiteUser(AbstractUser):

    activation_key_expires = models.CharField(
        max_length=128,
        blank=True,
    )
    # другие поля класса

    def is_activated_profile(self):
        """
        Проверка профиля. Прошел ли подтверждение (email, tel, etc)
        """

        if now() <= self.activation_key_expires:
            return False
        else:
            return True
