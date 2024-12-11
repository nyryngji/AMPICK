from django.db import models

# Create your models here.
class Post(models.Model):
    color_palettes = models.TextField(blank=False)
    novel_atmo = models.TextField(blank=False)
    novel_genre = models.TextField(blank=False)
    patient = models.TextField(blank=False)