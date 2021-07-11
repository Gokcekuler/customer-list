from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Musteri(models.Model):
    tc=models.PositiveSmallIntegerField( validators=[ MinValueValidator(10000000000),MaxValueValidator(99999999999)], unique=True)
    isim=models.CharField(max_length=100)
    soyisim=models.CharField(max_length=100)
    telefon=models.PositiveSmallIntegerField(validators=[ MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    sehir=models.CharField(max_length=100)
    ilce=models.CharField(max_length=100)

    def __str__(self):
        return self.isim

    def get_absolute_url(self):
        return reverse('detail', kwargs= {'id': self.id})

    def get_create_url(self):
        return reverse('create')

    def get_update_url(self):
        return reverse('update', kwargs= {'id': self.id})

    def get_delete_url(self):
        return reverse('delete', kwargs= {'id': self.id})

