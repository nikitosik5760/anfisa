from django.db import models


class IceCream(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    on_main = models.BooleanField('На главную?', default=True)
    image = models.ImageField(
        upload_to='articles/', verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField( max_digits=10, decimal_places=3, verbose_name='Цена', default=1)
    quantity = models.IntegerField(verbose_name='Количевство', default=1)

    class Meta:
        ordering = ('name',)
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return f'{self.name}'
