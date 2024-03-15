# Generated by Django 4.2.7 on 2024-03-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адресс')),
                ('postcode', models.CharField(max_length=6, verbose_name='Индекс')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='еvent_images/')),
                ('date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('organization', models.ManyToManyField(related_name='events', to='event.organization')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ('date',),
            },
        ),
    ]
