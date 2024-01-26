from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # Поле для ввода даты и времени

    class Meta:  # Мета класс - Это класс, который содержит дополнительную информацию о модели
        db_table = 'cars'  # Название таблицы в базе данных (по умолчанию appname_classname (post_hashtag))
        verbose_name = 'Car'  # Название модели в единственном числе
        verbose_name_plural = 'Cars'  # Название модели во множественном числе

    def __str__(self):
        return self.name