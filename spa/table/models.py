from django.db import models


class Entry(models.Model):
    date = models.CharField(max_length=20, verbose_name='Дата')
    title = models.CharField(max_length=255, verbose_name='Название')
    amount = models.BigIntegerField(verbose_name='Количество')
    distance = models.BigIntegerField(verbose_name='Расстояние')
