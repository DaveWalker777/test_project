from django.db import models


class Person(models.Model):
    Surname = models.CharField('Фамилия', max_length=50)
    Name = models.CharField('Имя', max_length=50)
    Middlename = models.CharField('Отчество', max_length=50)
    rank = models.ForeignKey('Rank', on_delete=models.PROTECT, verbose_name='Должность')
    Employed = models.DateField('Дата')


    def __str__(self):
        return self.Surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Rank(models.Model):
    Rank = models.CharField('Должность')

    def __str__(self):
        return self.Rank

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'