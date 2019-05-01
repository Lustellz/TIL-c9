from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)