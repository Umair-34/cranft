from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', signin, name="login"),
    path('signout', signout, name="signout"),
    path('signup', signup, name="signup"),
    path('change-password', change_password, name="change-password"),
    path('password_reset/', password_reset_request, name="password_reset"),
    path('email-activation/', email_message, name="email-activation"),
]