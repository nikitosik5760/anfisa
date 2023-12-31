# Generated by Django 4.2.3 on 2023-07-07 18:33

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0006_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(null=True, upload_to='ice_cream/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной')),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ice_cream.icecream', verbose_name='Мороженое')),
            ],
        ),
    ]
