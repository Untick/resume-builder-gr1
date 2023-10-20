from django.core.management.base import BaseCommand
from app_Promt.models import Category, Post

class Command(BaseCommand):
    def handle (self, *args, **options):

        #print ('Привет')

        # Выбираем все категории
        categories = Category.objects.all()
        # Выводим результат в виде QuerySet  - аналог списка
        print(categories)
        print(type(categories))
        # В цикле идем по всем элементам и выводим их, тип и значение
        for item in categories:
            print(item)
            print(item.name)
            print(type(item))
        print("End")


# Первый пост
post = Post.objects.first()
print(post.name)
print(post.text)

# Получим категорию связанную с постом
category = post.category
# Выведем её имя и тип
print(category.name)
print(type(category))

# Создание
category = Category.objects.create(name='Новая', description = "Что то")
print('Создали')

# Изменение
category = Category.objects.get(name='Новая')
category.name = 'Изменения'
category.save()
print('Изменили')

# Удаление
# Можно одну
category.delete()
print("Удалили")
# Можно несколько
#category.objects.all().delete()
# Проверяем, что всё удалось
categories = Category.objects.all()
# Выводим результат в виде QuerySet - это аналог списка
print(category)
