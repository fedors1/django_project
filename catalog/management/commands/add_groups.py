from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Кастомная команда для заполнения базы данных группами"

    def handle(self, *args, **options):
        call_command("loaddata", "product_manage.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
