from django.db import models

# Create your models here.

class Music(models.Model):
    singer_photo = models.ImageField(blank=True)
    singer_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)