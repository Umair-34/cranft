from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='profile_images/', verbose_name="Profile Picture")
    PhoneNumber = PhoneNumberField()
    Tagline = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.User} {self.PhoneNumber}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
