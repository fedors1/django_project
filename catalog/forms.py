import re

from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

DANGERS = {
    "CASINO": "казино",
    "CRYPTO_ONE": "крипта",
    "CRYPTO_TWO": "криптовалюта",
    "BIRZHA": "биржа",
    "LOWER": "дешево",
    "FREE": "бесплатно",
    "LIE": "обман",
    "POLICE": "полиция",
    "RADAR": "радар",
}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Цена продукта не может быть меньше или равна нулю.")
        elif not isinstance(price, (int, float)):
            raise ValidationError("Данное поле должно содержать числовое значение.")
        else:
            return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for v in DANGERS.values():
            if name and description:
                if re.findall(v, name, flags=re.I):
                    self.add_error(
                        "name", f"Данное поле не может содержать значение '{v}'."
                    )
                elif re.findall(v, description, flags=re.I):
                    self.add_error(
                        "description", f"Данное поле не может содержать значение '{v}'."
                    )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "type": "checkbox"}
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену продукта"}
        )
