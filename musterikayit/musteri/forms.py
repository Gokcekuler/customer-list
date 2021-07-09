from django import forms
from .models import Musteri

class MusteriForm(forms.ModelForm):
    class Meta:
        model=Musteri
        fields= [
                'tc',
                'isim',
                'soyisim',
                'telefon',
                'sehir',
                'ilce',
        ]


