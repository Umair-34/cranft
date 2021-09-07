from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContentForm, ProfileForm, ContactForm
from accounts.models import Profile
from django.core.files.images import get_image_dimensions


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def BlogList(request):
    queryset = Blog.objects.all()
    context = {
        'obj': queryset,
    }
    return render(request, 'core/blog_list.html', context)


def BlogDetail(request, id):
    queryset = Blog.objects.get(id=id)
    context = {
        'obj': queryset,
    }
    return render(request, 'core/blog_detail.html', context)


@login_required()
def UserProfile(request):
    ProfilePicture = Profile.objects.get(User=request.user)
    Picture = ProfilePicture.Image
    queryset = Videos.objects.filter(User=request.user)
    print(queryset)
    context = {
        'profile': Picture,
        'obj': queryset,
    }
    return render(request, 'core/profile.html', context)


@login_required()
def EditProfile(request):
    profile = Profile.objects.get(User=request.user)
    if request.method == 'POST':
        form2 = ProfileForm(request.POST, request.FILES, instance=profile)
        if form2.is_valid():
            content = form2.save(commit=False)
            content.User = request.user
            content.save()
            return redirect('core:profile')
    else:
        form2 = ProfileForm(instance=profile)
    context = {
        'form': form2,
    }
    return render(request, 'core/edit_profile.html', context)


def Explore(request):
    queryset = Videos.objects.all()
    print(queryset)
    context = {
        'obj': queryset,
    }
    return render(request, 'core/explore.html', context)


@login_required()
def UploadContent(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.User = request.user
            content.save()
            obj = Videos.objects.get(pk=content.pk)
            width, height = get_image_dimensions(obj.Video.file)
            obj.width = width
            obj.height = height
            obj.save()
            return redirect('core:profile')
    else:
        form = ContentForm
    context = {
        'form': form,
    }
    return render(request, 'core/content.html', context)


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ContactForm
    context = {
        'form' : form,
    }
    return render(request, 'core/contact.html', context)
