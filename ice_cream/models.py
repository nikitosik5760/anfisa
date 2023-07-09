from django.db import models
from django.contrib.admin import display
from django.utils.safestring import mark_safe


from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


class IceCream(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    on_main = models.BooleanField('На главную?', default=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=3, verbose_name='Цена', default=1)
    quantity = models.IntegerField(verbose_name='Количевство', default=1)

    class Meta:
        ordering = ('name',)
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    ice_cream = models.ForeignKey(
        IceCream, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self) -> str:
        return f'{self.ice_cream.name} - {self.content}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('-created_at',)


class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзыв'
        ordering = ('-created_at',)


class Image(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='ice_cream/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 200)],
        format='JPEG',
        options={'quality': 100},
    )
    ice_cream = models.ForeignKey(
        to=IceCream,
        verbose_name='Мороженое',
        on_delete=models.CASCADE,
        related_name='images'
    )
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    @display(description='')
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f"<img src='{self.image_thumbnail.url}' height=70>")

    @display(description='')
    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f"<img src='{self.image_thumbnail.url}'>")
