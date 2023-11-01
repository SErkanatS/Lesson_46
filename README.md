# Создание Собственной Модели Пользователя в Django

Создание собственной модели пользователя в Django позволяет более гибко определить поля пользователя и использовать стандартный менеджер пользователя. Вот как создать собственную модель пользователя:

## Шаг 1: Создайте новый проект Django или используйте существующий.

Если у вас еще нет проекта Django, создайте его с помощью команды:

```bash
django-admin startproject project_name
```

## Шаг 2: Создайте новое Django приложение.
Создайте новое приложение в вашем проекте с помощью команды:
```bash
python manage.py startapp app
```

## Шаг 3: Определите модель пользователя.
Внутри вашего приложения определите модель пользователя. В файле models.py вашего приложения определите модель, которая будет наследоваться от AbstractUser. 
Вот пример:
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='Пол')
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='Аватар')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
```

## Шаг 4: Обновите настройки проекта.
В файле settings.py вашего проекта добавьте настройку для вашей собственной модели пользователя:
```python
AUTH_USER_MODEL = 'app_name.CustomUser'
```

Замените 'app_name' на имя вашего приложения.

## Шаг 5: Создайте и примените миграции.
Создайте миграции для вашей модели с помощью команды:
```bash
python manage.py makemigrations
```
Примените миграции с помощью команды:
```bash
python manage.py migrate
```

## Шаг 6: Создайте форму регистрации.
Создайте форму регистрации для вашей модели пользователя. В файле forms.py вашего приложения определите форму. Пример:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'phone', 'gender', 'image')
```

## Шаг 7: Создайте представления и шаблоны.
Создайте представления для регистрации и шаблоны для этих представлений. Вы можете использовать стандартные представления Django или создать собственные.

## Шаг 8: Обновите URL-пути.
Обновите URL-пути вашего приложения, чтобы указать на представления регистрации.

## Шаг 9: Создайте и примените миграции для других моделей.
Если у вас есть дополнительные модели, которые имеют отношение к вашей модели пользователя, создайте и примените миграции для них.

## Шаг 10: Создайте суперпользователя.
Создайте суперпользователя с помощью команды:
```bash
python manage.py createsuperuser
```