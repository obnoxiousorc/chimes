from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()


class ChimesSet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Chime(models.Model):
    home_position = models.IntegerField(default=0)
    kit_location = models.IntegerField()
    note_name = models.CharField(max_length=10)
    chimes_set = models.ForeignKey(ChimesSet, on_delete=models.CASCADE)

