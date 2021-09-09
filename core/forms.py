from django import forms
from .models import Videos, Contact
from accounts.models import Profile


class ContentForm(forms.ModelForm):
    class Meta:
        model = Videos
        exclude = ('User', 'width', 'height')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Your Name',}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Your Email',}
        self.fields['subject'].widget.attrs = {'class': 'form-control', 'placeholder': 'Subject',}
        self.fields['message'].widget.attrs = {'class': 'form-control', 'placeholder': 'Message',}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("Image", "PhoneNumber", "Tagline", "Cover")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['PhoneNumber'].widget.attrs = {'class': 'form-control',  'placeholder': 'Contact Number',}
        self.fields['Tagline'].widget.attrs = {'class': 'form-control', 'placeholder': 'Tag Line', }
