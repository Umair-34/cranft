from django.urls import path
from .views import index, BlogList, BlogDetail

app_name = 'core'

urlpatterns = [
    path('',index, name='home'),
    path('blog-list',BlogList, name='bloglist'),
    path('blog-detail/<int:id>/',BlogDetail, name='blogdetail'),
]