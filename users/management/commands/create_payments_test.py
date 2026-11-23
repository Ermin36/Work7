from django.core.management import BaseCommand

from users.models import Payments, User
from materials.models import Course, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):

        user, _ = User.objects.get_or_create(email='test@example.com', phone_number='+12345678901', city='test')
        user.set_password('test')
        user.save()

        course, _ = Course.objects.get_or_create(
            title='Тестовый курс',
            defaults={'description': 'Тест системы'},
        )

        lesson, _ = Lesson.objects.get_or_create(
            title='Тестовый урок',
            video_url='https://example.com/video/',
            description='Тестовый урок для теста системы'
        )

        Payments.objects.create(
            user=user,
            course=course,
            amount=135,
            payment_method='cash',
        )

        Payments.objects.create(
            user=user,
            lesson=lesson,
            amount=120,
            payment_method='transfer',
        )

        self.stdout.write(self.style.SUCCESS(
            f'Тестовые платежи созданы.'
        ))