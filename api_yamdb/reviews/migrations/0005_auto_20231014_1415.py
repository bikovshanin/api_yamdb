# Generated by Django 3.2 on 2023-10-14 11:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(help_text='Поставьте оценку от 1 до 10.', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
    ]