from django.urls import path
from .views import index, BlogList

urlpatterns = [
    path('',index, name='home'),
    path('blog-list',BlogList, name='blog-list'),
]