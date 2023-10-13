from django.db import models

# Create your models here.

class Students(models.Model):
    REC_ID =      models.TextField()                        # bigint    # Идентификатор записи
    TIMESTAMP =   models.DateTimeField(auto_now_add=True)   # timestamp # Метка    времени    записи
    STUDENT_ID =  models.TextField()                        # int       # Идентификатор    студента
    LOGIN =       models.TextField(blank=True)              # text      # Логин    пользователя
    PWD =         models.TextField(blank=True)              # text      # Хэш - значение    пароля
    NAME =        models.TextField(blank=True)              # text      # Имя
    SURNAME =     models.TextField(blank=True)              # text      # Фамилия
    PATRONYMIC =  models.TextField(blank=True)              # text      # Отчество
    PHOTO =       models.BinaryField()                      # bytea     # Фотография
    GENDER =      models.BooleanField()                     # boolean   #  Пол    человека(0 - женский, 1 - мужской)
    BIRTHDATE =   models.DateTimeField()                    # date      #  Дата    рождения
    EMAIL =       models.TextField(blank=True)              # text      # Адрес    электронной    почты
    PHONE =       models.TextField(blank=True)              # text      # Контактный    телефон
    RESIDENCY =   models.TextField(blank=True)              # text      # Место    жительства
    STATUS =      models.BinaryField()                      # smallint  # Статус(0 - студент, 1 - выпускник, …)