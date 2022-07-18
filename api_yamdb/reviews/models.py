from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(
        unique=True, verbose_name='Отображение названия категории',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=256, verbose_name='Жанр')
    slug = models.SlugField(
        unique=True, verbose_name='Отображение жанра',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title
