from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Кастомная команда для заполнения базы данных группами"

    def handle(self, *args, **options):
        moderator_product, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS("Группа 'модератор продуктов' успешно создана!")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Группа 'модератор продуктов' уже существует!")
            )

        can_unpublish_product = Permission.objects.get(codename="delete_product")
        can_remove_product = Permission.objects.get(codename="change_product")

        moderator_product.permissions.add(can_unpublish_product, can_remove_product)
        self.stdout.write(self.style.SUCCESS("Разрешения добавлены к группе"))
