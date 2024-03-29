# Тестовое задание
[![License MIT](https://img.shields.io/badge/licence-MIT-green)](https://opensource.org/license/mit/)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)


### Описание
1.	Создать проект и приложение на Django Rest Framework >= 3.12 (Django > =3.2).
2.	Реализовать возможность хранения номера телефона пользователя.
3.	Использовать email и пароль при создании и авторизации пользователя.
4.	Использовать JWT Token для аутентификации пользователя.
5.	Создать модель Организации со следующими полями: title, description, address, postcode.
6.	Создать модель Мероприятия со следующими полями: title, description, organizations, image, date.
7.	Создать чат между пользователями использую технологию Web Socket.
8.	Использовать для запуска проекта Docker.

Дополнительное описание:
При создании пользователя не нужно использовать подтверждение по почте. Пользователи состоят в организациях. Одно мероприятие могут организовывать несколько организаций. Настроить панель администратора (добавить фильтрацию и поиск), при просмотре мероприятия выводить превью изображения. Вывод информации и создание записей по api доступно только зарегистрированным пользователям. При создании мероприятия необходимо использовать sleep 60 секунд и данный запрос не должен быть блокирующим. 

Конечные точки:
1.	Создание организации
2.	Создание мероприятия
3.	Вывод мероприятия с информацией о всех действующих пользователей, которые участвуют в организации мероприятия с разбивкой по организациям (вывести информацию о организации с объединением почтового индекса и адресом).
4.	Вывод мероприятий с возможностью фильтрации и сортировки по дате, поиском по названию и лимитной пагинацией.

# Пример API 
### Регистрирует пользователя в системе
POST .../api/users/

| Parameter | Type     | Description                        |
|:----------| :------- |:-----------------------------------|
| `email`   | `string` | **Обязательно**. Электронная почта |
| `password` | `string` | **Обязательно**. Пароль            |
| `telephone` | `string` | **Не обязательно**. Телефон    |

### Вход в систему 
POST .../api/token/login/

| Parameter | Type     | Description                        |
|:----------| :------- |:-----------------------------------|
| `email`   | `string` | **Обязательно**. Электронная почта |
| `password` | `string` | **Обязательно**. Пароль            |

### Обновление токена
POST .../api/jwt/refresh/

| Parameter | Type     | Description                        |
|:----------| :------- |:-----------------------------------|
| `refresh`   | `string` | **Обязательно**. Токен  |

### Создание новой организации
POST .../api/organizations/

| Parameter | Type     | Description                        |
|:----------| :------- |:-----------------------------------|
| `title`   | `string` | **Обязательно**. Название |
| `description` | `string` | **Обязательно**. Описание    |
| `address` | `string` | **Обязательно**. Адресс           |
| `postcode` | `string` | **Обязательно**. Почтовый код   |


### Создание нового мероприятия
POST .../api/events/

| Parameter | Type     | Description                        |
|:----------| :------- |:-----------------------------------|
| `title`   | `string` | **Обязательно**. Название |
| `description` | `string` | **Обязательно**. Описание    |
| `organization` | `string` | **Не обязательно**. Организации     |
| `date` | `string` | **Обязательно**. Дата в формате 23.01.2024 18:45   |
| `image` | `string` | **Не обязательно**. Картинка ф формате base64  |

### Вывод списка мероприятий
GET .../api/events/?search=$(query_search)
                                     &ordering=$(ordering_fields)
                                     &limit=$(query_limit)
                                     &$(filter_method)=$(filter_data)

### Вывод  мероприятия
GET .../api/events/$(id)



## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:TSergey1/test_api.git
```
### Запускаем проект:
```
docker-compose up
```

## Вебсокет чат
Чат - ws://0.0.0.0:8000/chat/

Подключение по JWT token

Передача сообщений в формате JSON
{
    "user": "user@user.ru",
    "message": "Текст сообщения"
}
