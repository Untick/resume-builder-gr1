from django.db import models

# Create your models here.

class CV(models.Model):
    REC_ID =           models.TextField()                       # bigint    # Идентификатор записи
    TIMESTAMP =        models.DateTimeField(auto_now_add=True)  # timestamp # Метка    времени    записи
    STUDENT_ID =       models.TextField()                       # int       # Идентификатор    студента
    CV_ID =            models.TextField()                       # int       # Идентификатор    резюме
    CV_NAME =          models.TextField()                       # int       # Название    резюме
    CV_PATTERN =       models.TextField()                       # int       # Шаблон    резюме
    TARGET_POSITION =  models.TextField(blank=True)             # text      # Желаемая    должность
    TARGET_SALARY =    models.TextField()                       # real      # Желаемая    зарплата
    EMPLOYMENT_FORM =  models.TextField(blank=True)             # text      # форма    занятости (полный    или    сокращённый    рабочий    день, проектная    работа, разовое    задание)
    WORKPLACE =        models.TextField(blank=True)             # text      # Место    работы(офис, удалённо, смешанный)
    BUSINESS_TRIP =    models.BooleanField(default=False)       # boolean   # Готовность к командировкам
    RELOCATE =         models.BooleanField(default=False)       # boolean   # Готовность к переезду
    FOREIGN_LANG =     models.TextField(blank=True)             # text      # Знание иностранных языков
    SKILLS =           models.TextField(blank=True)             # text      # Ключевые навыки
    STRENGTHS =        models.TextField(blank=True)             # text      # Сильные стороны
    EXPERIENCE =       models.TextField(blank=True)             # text      # Опыт работы
    EDUCATION =        models.TextField(blank=True)             # text      # Образование
    CERTIFICATES =     models.TextField(blank=True)             # text      # Сертификаты
    PUBLICATIONS =     models.TextField(blank=True)             # text      # Публикации
    ACHIEVEMENTS =     models.TextField(blank=True)             # text      # Достижения
    REFERENCES =       models.TextField(blank=True)             # text      # Cсылки на ресурсы
    RECOMMENDATIONS =  models.TextField(blank=True)             # text      # Рекомендации
    HOBBIES =          models.TextField(blank=True)             # text      # Хобби
    ABOUT =            models.TextField(blank=True)             # text      # О себе
    COVER_LETTER =     models.TextField(blank=True)             # text      # Сопроводительное письмо