from django.shortcuts import render,redirect
from .models import Song, Podcast, Audiobook 
from rest_framework import viewsets
from .serializers import SongSerializers, PodcastSerializers, AudiobookSerializers

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializers

class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializers
