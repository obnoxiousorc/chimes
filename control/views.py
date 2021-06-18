from datetime import datetime

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from .models import Song

from control import task_queue
import logging

logger = logging.getLogger('django')

def index(request):
    return HttpResponse(serializers.serialize('json', Song.objects.all()), 'application/json')

def new_song(request):
    POST = request.POST
    song = Song.objects.create(
        name=POST['name'],
        artist=POST['artist'],
        data=POST['song'],
        created_at=datetime.now()
    )
    return HttpResponse(serializers.serialize('json', [song]))

def all_songs(request):
    songs = Song.objects.all()
    return HttpResponse(serializers.serialize('json', songs))

def play_song(request, pk):
    song = None
    try:
        song = Song.objects.get(pk=pk)
    except:
        return HttpResponse(status=500)
    task_queue.q.put(song)
    return HttpResponse()