from django.contrib import admin
from musteri.models import Musteri


class MusteriAdmin(admin.ModelAdmin):
    list_display=['tc','isim','soyisim','telefon','sehir','ilce']
                
    search_fields=['tc','isim','soyisim','telefon','sehir','ilce']
    list_editable=['isim','soyisim','telefon','sehir','ilce']

    class Meta:
        model= Musteri

admin.site.register(Musteri,MusteriAdmin)


# Register your models here.
