from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    Модель блоговой записи
    """
    header = models.CharField(max_length=35, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Содержимое статьи")
    preview = models.ImageField(upload_to="blogs/images/", verbose_name="Фото", null=False, default="Изображение отсутствует")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Статус публикации")
    views_counter = models.IntegerField(default=0, verbose_name="Количество просмотров")


    def __str__(self):
        return f"Название: {self.header}, количество просмотров: {self.views_counter}"


    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
