# Generated by Django 3.2.5 on 2021-07-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteri',
            name='ilce',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musteri',
            name='isim',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musteri',
            name='sehir',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musteri',
            name='soyisim',
            field=models.CharField(max_length=100),
        ),
    ]