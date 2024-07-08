from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    summary = models.CharField(max_length=50, verbose_name='Краткое описание')
    description = models.TextField(max_length=100, verbose_name='Полное описание', null=True, blank=True)
    status = models.ForeignKey('webapp.Status', verbose_name='Статус', on_delete=models.PROTECT)
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, verbose_name='Тип')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return self.summary
