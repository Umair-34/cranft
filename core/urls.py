from django.urls import path
from .views import index, BlogList, BlogDetail, UserProfile, EditProfile, Explore, UploadContent, Contact

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('explore', Explore, name='explore'),
    path('contact-us', Contact, name='contact'),
    path('upload', UploadContent, name='content'),
    path('blog-list', BlogList, name='bloglist'),
    path('user-profile/', UserProfile, name='profile'),
    path('blog-detail/<int:id>/', BlogDetail, name='blogdetail'),
    path('edit-profile/', EditProfile, name='editprofile'),
]
