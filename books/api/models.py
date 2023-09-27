from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

User = get_user_model()


class Author(AbstractBaseUser):
    username = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Никнейм'
    )
    first_name = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилия'
    )
    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
        unique=True,
        null=False
    )
    author = models.ManyToManyField(Author, related_name='books')

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('title',),
                name='unique_author_book'
            ),
        )
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.pk}'
