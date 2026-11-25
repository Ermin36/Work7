from django.db import models

from config import settings


# Create your models here.
class Course(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(default='default.jpeg', upload_to='courses/%Y/%m', verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('title',)


class Lesson(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name="Автор")
    preview = models.ImageField(
        upload_to='lessons/previews/',
        blank=True,
        null=True,
        verbose_name='Превью (картинка)',
    )
    video_url = models.URLField(
        max_length=500,
        verbose_name='Ссылка на видео',
    )
    courses = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курсы',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('title',)