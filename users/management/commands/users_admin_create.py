from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создаёт суперпользователя admin@example.com'

    def handle(self, *args, **options):
        email = 'admin@example.com'
        password = 'admin.'

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(
                f'Суперпользователь {email} уже существует, пропускаю создание.'
            ))
            return

        user = User.objects.create_superuser(email=email, password=password)

        self.stdout.write(self.style.SUCCESS(
            f'Суперпользователь {user.email} создан.'
        ))
