from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=3000)

    class Meta:
        abstract = True


class Organization(BaseModel):
    """Модель организации"""
    address = models.CharField('Адресс', max_length=255)
    postcode = models.CharField('Индекс', max_length=6)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.title


class Event(BaseModel):
    """Модель мероприятия"""
    organization = models.ManyToManyField(
        'Organization',
        related_name='events',
    )
    image = models.ImageField(
        upload_to='еvent_images/',
        blank=True,
        null=True,
    )
    date = models.DateTimeField('Дата мероприятия')

    class Meta:
        ordering = ('date',)
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title
