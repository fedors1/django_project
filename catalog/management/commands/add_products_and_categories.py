from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Кастомная команда для наполнения db тестовыми данными."

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1, _ = Category.objects.get_or_create(
            name="Смартфоны", description="Компактные устройства связи"
        )
        category2, _ = Category.objects.get_or_create(
            name="Телевизоры",
            description="Предназначены для демонстрации различного рода информации на экране",
        )

        products = [
            {
                "name": "Iphone 16",
                "description": "Мощный и элегантный телефон из новой линейки apple",
                "image": "iphone.png",
                "category": category1,
                "price": 100000,
            },
            {
                "name": "Samsung",
                "description": "Новый смартфон всеми известной марки Samsung",
                "image": "samsung.png",
                "category": category1,
                "price": 98000,
            },
            {
                "name": "Haier",
                "description": "чайхана телевизор",
                "image": "haier.png",
                "category": category2,
                "price": 78000,
            },
            {
                "name": "LG",
                "description": "Хороший телек корейской марки LG",
                "image": "lg.png",
                "category": category2,
                "price": 83000,
            },
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {product.name} {product.price}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.name} {product.price}"
                    )
                )
