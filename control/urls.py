from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_song, name='new'),
    path('', views.index, name='index'),
    path('all_songs', views.all_songs, name='all_songs'),
    path('song/<int:pk>/play', views.play_song, name='play_song'),
]
