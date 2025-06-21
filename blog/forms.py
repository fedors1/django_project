import re

from django import forms

from blog.models import Blog

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


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["created_at", "is_active", "views_counter"]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get("header")
        description = cleaned_data.get("description")

        for v in DANGERS.values():
            if header and description:
                if re.findall(v, header, flags=re.I):
                    self.add_error(
                        "header", f"Данное поле не может содержать значение {v}"
                    )
                elif re.findall(v, description, flags=re.I):
                    self.add_error(
                        "description", f"Данное поле не может содержать значение {v}"
                    )

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields["header"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название статьи"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание статьи"}
        )

        self.fields["preview"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
