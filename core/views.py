from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContentForm


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
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.User = request.user
            content.save()
    else:
        form = ContentForm
    return render(request, 'core/profile.html', {'form': form})
