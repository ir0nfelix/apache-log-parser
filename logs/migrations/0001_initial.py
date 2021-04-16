# Generated by Django 3.2 on 2021-04-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата лога')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('method', models.CharField(max_length=7, verbose_name='Метод')),
                ('uri', models.CharField(default='/', max_length=10000, verbose_name='URI')),
                ('response_code', models.SmallIntegerField(verbose_name='Код ответа')),
                ('response_size', models.IntegerField(default=0, verbose_name='Размер ответа')),
                ('details', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Детали')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
                'ordering': ('-datetime',),
            },
        ),
    ]
