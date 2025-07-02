from django.db import models


class Category(models.Model):
    """
    Модель категории
    """

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
        upload_to="products/images/", verbose_name="Фотография продукта", blank=True
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, verbose_name="Категория продукта"
    )
    price = models.IntegerField(verbose_name="Цена продукта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"Название: {self.name}, Цена за шт. {self.price} р."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
