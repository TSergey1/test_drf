import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from event.models import Organization


class UserManager(BaseUserManager):
    """Переопределяем мэнеджер пользователя"""

    def create_user(self, email, password, **kwargs):
        """Создает и возвращает пользователя с email и password"""
        if email is None:
            raise TypeError('У пользователя должен быть email.')
        user = self.model(email=email, password=password, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """Создает и возввращет пользователя с привилегиями суперадмина"""
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""
    email = models.EmailField(
        max_length=50,
        db_index=True,
        unique=True,
        verbose_name='email',
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон'
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    organizations = models.ManyToManyField(Organization, related_name='users')
    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token,
        вместо user._generate_jwt_token()
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
