from django.db import models
from django.core.validators import FileExtensionValidator




class TelegramBot(models.Model): 

    id_user = models.IntegerField(default =1)
    name_user = models.CharField(verbose_name='Имя', max_length=255, blank=True)
    phone_user = models.CharField(verbose_name='Телефон', max_length=255, blank=True)
    group = models.CharField(verbose_name='Группа', max_length=255, blank=True)
    course = models.CharField(verbose_name='Курс', max_length=100, blank=True)
    
    def __str__(self):
        return self.id_user
