from django.db import models


class TelegramBot(models.Model): 
    id_user = models.IntegerField()
    name_user = models.CharField(verbose_name='Имя', max_length=255, null= True, blank=True)
    course = models.IntegerField(verbose_name='Курс',null= True,blank=True)
    group = models.CharField(verbose_name='Группа', max_length=255, null= True,blank=True)
    phone_user = models.CharField(verbose_name='Телефон', max_length=255,null= True, blank=True)
    answer = models.CharField(verbose_name='Ответ на рассылку', max_length=255,null= True, blank=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return f'{self.id_user} {self.phone_user}' 
    
    
class Sendings(models.Model): 
    id_sending = models.IntegerField()
    text = models.CharField(verbose_name='Текст', max_length=255, null= True, blank=True)
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

       
    
   
