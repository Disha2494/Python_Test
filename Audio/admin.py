from django.contrib import admin
from . import models

class SongAdmin(admin.ModelAdmin):
    list_display = ("name","duration_in_sec","uploaded_time")

class PodcastAdmin(admin.ModelAdmin):
    list_display=("name","duration_in_sec","uploaded_time", "host","participants")

class AudiobookAdmin(admin.ModelAdmin):
    list_display=("title", "author", "narrator", "duration_in_sec","uploaded_time")

admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Podcast, PodcastAdmin)
admin.site.register(models.Audiobook, AudiobookAdmin)

