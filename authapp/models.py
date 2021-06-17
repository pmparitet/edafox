from django.db import models
from django.contrib.auth.models import AbstractUser


class FoxUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
    )

    email = models.EmailField(verbose_name='Email', unique=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    gender = models.CharField(max_length=1, verbose_name='пол', blank=True, choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, default='1900-01-01')
    phone_number = models.CharField(max_length=15, verbose_name='телефон', blank=True)

