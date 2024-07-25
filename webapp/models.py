from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def summary_valid(value):
    if len(value) < 10:
        raise ValidationError('Не может быть меньше 10 символов')


def description_valid(value):
    if 'Project' in value.capitalize():
        raise ValidationError('Нельзя такое писать :)')


class Task(models.Model):
    summary = models.CharField(max_length=50, verbose_name='Краткое описание', validators=[summary_valid])
    description = models.TextField(max_length=100, verbose_name='Полное описание', null=True, blank=True,
                                   validators=[description_valid])
    status = models.ForeignKey('webapp.Status', verbose_name='Статус', on_delete=models.PROTECT)
    type = models.ManyToManyField('webapp.Type', verbose_name='Тип', related_name='task')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='tasks',
                                verbose_name='Проект')

    def __str__(self):
        return self.summary


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=100, verbose_name='Описание')
    users = models.ManyToManyField(get_user_model(), related_name='projects', verbose_name='Пользователь', null=True,
                                   blank=True)
    created_date = models.DateField(verbose_name='Дата создания')
    updated_date = models.DateField(verbose_name='Дата обновления', null=True, blank=True)

    def __str__(self):
        return self.name
