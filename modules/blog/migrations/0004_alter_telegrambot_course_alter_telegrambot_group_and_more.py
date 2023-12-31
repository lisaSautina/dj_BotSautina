# Generated by Django 5.0 on 2023-12-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_telegrambot_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegrambot',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='telegrambot',
            name='group',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='telegrambot',
            name='name_user',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='telegrambot',
            name='phone_user',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон'),
        ),
    ]
