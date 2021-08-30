from django.urls import path
from .views import index, BlogList, BlogDetail, UserProfile

app_name = 'core'

urlpatterns = [
    path('',index, name='home'),
    path('blog-list',BlogList, name='bloglist'),
    path('user-profile/', UserProfile, name='profile'),
    path('blog-detail/<int:id>/',BlogDetail, name='blogdetail'),
]