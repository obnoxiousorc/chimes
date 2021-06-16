from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    data = models.TextField()
