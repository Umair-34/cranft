from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


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
