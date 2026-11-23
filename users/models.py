from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from materials.models import Lesson, Course


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff', False) is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser', False) is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(default='default.jpeg', upload_to='media/', blank=True)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=30)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='payments', verbose_name='Пользователь')
    date_payment = models.DateField(auto_now_add=True, verbose_name='Дата платежа')
    lesson = models.ForeignKey(Lesson,
        on_delete=models.PROTECT,
        related_name='payments',
        verbose_name='Уроки',
        blank=True,
        null=True,)
    course = models.ForeignKey(Course,
        on_delete=models.PROTECT,
        related_name='payments',
        verbose_name='Курсы',
        blank=True,
        null=True,)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа')
    METHOD_CHOICES = (
        ('cash', 'Наличный'),
        ('transfer', 'Перевод на счёт')
    )
    payment_method = models.CharField(choices=METHOD_CHOICES, max_length=10, verbose_name='Тип платежа')

    def __str__(self):
        return f'{self.user.email} ({self.date_payment}): {self.amount}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
