from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
