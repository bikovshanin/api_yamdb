# Generated by Django 3.2 on 2023-10-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]