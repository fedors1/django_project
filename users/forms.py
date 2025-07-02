from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", )

    def clean_phone_number(self):
        """ """
        phone_number_valid = self.cleaned_data["phone_number"]
        if phone_number_valid and not phone_number_valid.isdigit():
            raise ValidationError(
                "Номер телефона не может содержать не числовые значения."
            )
        return phone_number_valid


class CustomUserRegistrationForm(AuthenticationForm):
    """Форма аутентификации пользователя"""
    pass
