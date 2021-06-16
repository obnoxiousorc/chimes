from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_song, name='new'),
    path('', views.index, name='index'),
]
