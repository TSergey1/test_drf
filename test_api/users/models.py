from django.contrib.auth.models import AbstractUser
from django.db import models

from event.models import Organization


class User(AbstractUser):
    """Модель пользователя"""
    EMAIL_FIELD = 'username'

    username = models.EmailField(
        unique=True,
        verbose_name='email',
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон'
    )
    organizations = models.ManyToManyField(Organization, related_name='users')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.username
