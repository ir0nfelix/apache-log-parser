from django.db import models


class LogEntity(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата лога')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    method = models.CharField(verbose_name='Метод', max_length=7)
    uri = models.CharField(verbose_name='URI', max_length=10000, default='/')
    response_code = models.SmallIntegerField(verbose_name='Код ответа')
    response_size = models.IntegerField(verbose_name='Размер ответа', default=0)
    details = models.CharField(verbose_name='Детали', max_length=10000, blank=True, null=True)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        ordering = ('-datetime',)
