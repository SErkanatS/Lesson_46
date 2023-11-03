from django.contrib.auth.models import AbstractUser, User
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='Пол')
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='Аватар')
    
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        


