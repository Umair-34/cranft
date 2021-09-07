from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Videos(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    Video = models.FileField(upload_to='videos')
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.User}'

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'


class Blog(models.Model):
    Date = models.DateField(auto_now_add=True)

    Title = models.CharField(max_length=5000)
    Image = models.ImageField(upload_to='blog_images/', default='blog_images/default.png')
    Tagline = models.CharField(max_length=150, null=False, blank=False)

    Content = models.TextField(null=False, blank=False)
    Author = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'{self.Date} {self.Title}'

    def get_absolute_url(self):
        return reverse('core:blogdetail', args=f'{self.id}')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} {self.subject}'

    class Meta:
        verbose_name = 'Queries'
        verbose_name_plural = 'Queries'
