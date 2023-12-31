# Generated by Django 4.2.3 on 2023-07-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_icecream_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количевство'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='Изображение'),
        ),
    ]
