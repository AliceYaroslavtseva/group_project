# Generated by Django 3.2 on 2022-12-16 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, help_text='Имя', max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, help_text='Фамилия', max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, help_text='Пароль', max_length=150, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Nickname', max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Nickname должен содержать буквы,цифры и символы @.+-_', regex='^[\\w.@+-]+')], verbose_name='Логин'),
        ),
    ]
