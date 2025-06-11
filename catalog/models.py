from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Название: {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """
    Модель продукта
    """

    name = models.CharField(max_length=25, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(
        upload_to="media/images", verbose_name="Фотография продукта"
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, verbose_name="Категория продукта"
    )
    price = models.IntegerField(verbose_name="Цена продукта")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Название: {self.name}, Цена за шт. {self.price} р."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
