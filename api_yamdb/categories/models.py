from django.db import models


class Categories(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(max_length=50)