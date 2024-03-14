from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import mark_safe

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

    @property
    def all_address(self):
        """Полный адресс с посткодом"""
        return f'{self.postcode} {self.address}'


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

    @property
    def admin_image(self):
        """Картинка для админки"""
        try:
            return mark_safe(
                '<img src="{}" width="100" height="100">'.format(self.image.url)
            )
        except ValueError:
            return None
