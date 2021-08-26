from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def BlogList(request):
    return render(request, 'core/blog_list.html')