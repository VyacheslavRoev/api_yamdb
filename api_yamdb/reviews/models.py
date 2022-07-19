from django.db import models
import datetime

from django.forms import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(
        unique=True, verbose_name='Отображение названия категории',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Жанр')
    slug = models.SlugField(
        unique=True, verbose_name='Отображение жанра',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


def validate_year(year):
    if year > datetime.date.year():
        raise ValidationError(
            (f'Год выпуска {year} больше текущего!'),
            params={'year': year},
        )


class Title(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(
        verbose_name='Год выпуска', validators=[validate_year]
    )
    description = models.CharField(
        max_length=256, verbose_name='Описание',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category, verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='categories',
        null=True
    )
    genre = models.ManyToManyField(
        Genre, verbose_name='Жанр',
        through='TitleGenre',
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title, verbose_name='Произведение',
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre, verbose_name='Жанр',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} {self.genre}'

    class Meta:
        verbose_name = 'Произведение и жанр'
        verbose_name_plural = 'Произведения и жанры'
