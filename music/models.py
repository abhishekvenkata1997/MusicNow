from django.db import models
from django.urls import reverse

# Create your models here.


class Album(models.Model):
      artist           = models.CharField(max_length=50)
      album_title      = models.CharField(max_length = 100)
      genre           = models.CharField(max_length=50)
      album_logo      = models.FileField()

      def __str__(self):
        return self.album_title + '- ' + self.artist

      # to add new albums and to get the primary key value into self
      def get_absolute_url(self):
            return reverse('music:detail', kwargs = {'pk': self.pk})

class Song(models.Model):
      album           = models.ForeignKey(Album,on_delete = models.CASCADE)
      file_type       = models.CharField(max_length=10)
      song_title      = models.CharField(max_length=200)
      song_length     = models.CharField(max_length=30)
      is_Favorite     = models.BooleanField(default = False)

      def __str__ (self):
            return self.song_title

      #while adding new songs to get primary key into self

      def get__absolute__url(self):
            return reverse ('music:index1' , kwargs = {'pk':self.pk})