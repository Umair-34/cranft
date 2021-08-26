from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Images(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.User}'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Videos(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Video = models.FileField(upload_to='videos')

    def __str__(self):
        return f'{self.User}'

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'


class Blog(models.Model):
    Date = models.DateField(auto_now_add=True)

    Title = models.CharField(max_length=5000, default='Title')
    Image = models.ImageField(upload_to='blog_images/', default='blog_images/default.png')

    Content = models.TextField()
    Author = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'{self.Date} {self.Title}'

    def get_absolute_url(self):
        return reverse('core:blog_detail', args=f'{self.Title}')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
