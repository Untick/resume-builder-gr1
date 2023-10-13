from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model): # Создадим модель для категории постов, наследуя свяойства класса django.db.models.Model
    # Id не надоб он создается автоматически
    # для имени модели выбираем тип поля CharField с максимальной длинной символов 16 и делим его уникальным
    name = models.CharField(max_length=16, unique=True)
    # Добавим описание категории, выбрав тип поля TextField; параметр blank=True указывает, что поле может быть пустым
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model): # Создадим класс постов
    # Для имени посто так же выбираем тип поля CharField, оно может быть длиннее - max_length = 32 и делаем его уникальным
    name = models.CharField(max_length=32, unique=True)
    # Добавляем непосредственно текст поста
    text = models.TextField()
    # Долбавляем дату создания поста и ее автозаполнение
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Устанавливаем связь с категорией: один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


