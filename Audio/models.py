from django.db import models
from django.utils import timezone
from django_mysql.models import ListCharField

# Create your models here.
def validate_date(uploaded_time):
    if uploaded_time < timezone.now().date():
        raise ValidationError("Date cannot be in the past")

class Song(models.Model):
    name = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    uploaded_time = models.DateField(default=timezone.now().strftime("%Y-%m-%d"), validators=[validate_date])
    
    def __str__(self):
        return self.name

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    uploaded_time = models.DateField(default=timezone.now().strftime("%Y-%m-%d"), validators=[validate_date])
    host = models.CharField(max_length=100)
    participants = ListCharField(
        blank=True,
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10*101),
    )

    def __str__(self):
        return self.name

class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    uploaded_time = models.DateField(default=timezone.now().strftime("%Y-%m-%d"), validators=[validate_date])

    def __str__(self):
        return self.title


