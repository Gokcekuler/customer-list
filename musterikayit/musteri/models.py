from django.db import models

from django.urls import reverse


class Musteri(models.Model):
    tc=models.PositiveSmallIntegerField()
    isim=models.CharField(max_length=100)
    soyisim=models.CharField(max_length=100)
    telefon=models.PositiveSmallIntegerField()
    sehir=models.CharField(max_length=100)
    ilce=models.CharField(max_length=100)


    def __str__(self):
        return self.isim

    def get_absolute_url(self):
        return reverse('detail', kwargs= {'id': self.id})

# Create your models here.
