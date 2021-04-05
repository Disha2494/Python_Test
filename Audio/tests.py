from django.test import TestCase
from .models import Song, Podcast, Audiobook

# Create your tests here.

class TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Song.objects.create(name='test_song', duration_in_sec=150, uploaded_time="2021-04-30")
        Podcast.objects.create(name='test_podcast', duration_in_sec=15, uploaded_time="2021-04-30", host="test", 
        participants=['test2', 'test1'])
        Audiobook.objects.create(title='test_book', author="test", narrator="test1", duration_in_sec=15, uploaded_time="2021-04-30")

    def test_song_content(self):
        song = Song.objects.get(id=1)
        name = f'{song.name}'
        duration = f'{song.duration_in_sec}'
        time = f'{song.uploaded_time}'
        self.assertEquals(name, 'test_song')
        self.assertEquals(duration, '150')
        self.assertEquals(time, '2021-04-30')

    def test_podcast_content(self):
        podcast = Podcast.objects.get(id=1)
        name = f'{podcast.name}'
        duration = f'{podcast.duration_in_sec}'
        time = f'{podcast.uploaded_time}'
        host = f'{podcast.host}'
        participant = f'{podcast.participants}'
        self.assertEquals(name, 'test_podcast')
        self.assertEquals(duration, '15')
        self.assertEquals(time, '2021-04-30')
        self.assertEquals(host, 'test')
        self.assertEquals(participant, "['test2', 'test1']")

    def test_audiobook_content(self):
        song = Audiobook.objects.get(id=1)
        name = f'{song.title}'
        author = f'{song.author}'
        narrator = f'{song.narrator}'
        duration = f'{song.duration_in_sec}'
        time = f'{song.uploaded_time}'
        self.assertEquals(name, 'test_book')
        self.assertEquals(author, 'test')
        self.assertEquals(narrator, 'test1')
        self.assertEquals(duration, '15')
        self.assertEquals(time, '2021-04-30')
