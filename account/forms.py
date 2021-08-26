from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):  # Extending UserCreationForm for registration
    username = forms.CharField(max_length=123, required=True)
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('User', 'Image')
        widgets = {
            # 'Image': forms.ImageField(attrs={'class': 'form-control'}),
            'PhoneNumber': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '+91 111 1234567', 'type': 'tel'}),
        }
