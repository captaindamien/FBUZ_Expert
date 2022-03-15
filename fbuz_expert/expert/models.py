from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Expertises(models.Model):
    exp_number = models.PositiveIntegerField(
        verbose_name='номер экспертизы',
        default=0,
    )
    doc_type = models.CharField(
        verbose_name='тип документа',
        max_length=100,
        blank=True,
    )
    object_name = models.TextField(
        verbose_name='наименование ЮЛ, ИП, объекта',
        blank=True,
    )
    exp_basis = models.TextField(
        verbose_name='основание экспертизы',
        blank=True,
    )
    exp_subject = models.TextField(
        verbose_name='предмет экспертизы',
        blank=True,
    )
    exp_result = models.TextField(
        verbose_name='результат экспертизы',
        blank=True,
    )
    executor_name = models.CharField(
        verbose_name='ФИО исполнителя',
        max_length=100,
    )
    recipient_name = models.CharField(
        verbose_name='ФИО получателя',
        max_length=100,
    )
    note = models.TextField(
        verbose_name='примечание',
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    created = models.DateField(
        default=timezone.now,
        verbose_name='создано',
    )
    media = models.FileField(
        verbose_name='',
        upload_to='exps/%Y/%m/',
        blank=True,
    )

    def __str__(self):
        return f'№ п/п: {self.exp_number} / {self.object_name}'


class Customer(models.Model):
    pass
