from django.db import models
from django.urls import reverse


class Table(models.Model):
    id_width = models.IntegerField(default = 2)
    name_width = models.IntegerField(default = 2)
    price_width = models.IntegerField(default = 2)
    release_date_width = models.IntegerField(default = 2)
    lte_exists_width = models.IntegerField(default = 2)

    id_name = models.CharField(max_length=50, blank=True, null=True)
    name_name = models.CharField(max_length=50, blank=True, null=True)
    price_name = models.CharField(max_length=50, blank=True, null=True)
    release_date_name = models.CharField(max_length=50, blank=True, null=True)
    lte_exists_name = models.CharField(max_length=50, blank=True, null=True)

    id_num = models.IntegerField(default = 1)
    name_num = models.IntegerField(default = 2)
    price_num = models.IntegerField(default = 3)
    release_num = models.IntegerField(default = 4)
    lte_num = models.IntegerField(default = 5)

    def __str__(self):
        return f'Таблица №{self.id}'

    class Meta:
        verbose_name = 'Параметры таблицы'
        verbose_name_plural = 'Параметры таблиц'

class Savepath(models.Model):
    field_name = models.FilePathField(path = None, blank=True, null=True)
    # def get_path(self):
    #     self.name_path = 'phones.csv'
    #     return self.name_path


