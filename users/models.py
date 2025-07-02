from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Введите ваш номер телефона",
    )
    country = models.CharField(blank=True, null=True, verbose_name="Страна проживания")
    image = models.ImageField(blank=True, null=True, upload_to="users/images/")

    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username"
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
