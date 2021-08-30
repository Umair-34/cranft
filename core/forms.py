from django import forms
from .models import Images, Videos


# class ImageForm(forms.ModelForm):
#     model = Images
#     exclude = ('User', )

class ContentForm(forms.ModelForm):
    class Meta:
        model = Videos
        exclude = ('User',)
