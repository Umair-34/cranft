from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from verify_email.email_handler import send_verification_email

from .forms import RegisterForm, ProfileForm

from django.http import HttpResponse


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return HttpResponse('already authenticated')
        # return redirect('core:home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        pform = ProfileForm(request.POST)
        print('post request')
        if form.is_valid() and pform.is_valid():
            print('form valid')
            inactive_user = send_verification_email(request, form)  # Send verification email to in-active user
            pinst = pform.save(commit=False)
            pinst.User = inactive_user
            pinst.save()
            return redirect('account:email-activation')
        else:
            print('form invalid')
            return render(request, 'account/signup.html', {'form': form, 'pform': pform})
    else:
        print('not post request')
        form = RegisterForm()
        pform = ProfileForm
        return render(request, 'account/signup.html', {'form': form, 'pform': pform})


def signin(request):
    error = ''
    if request.user.is_authenticated:
        # return redirect('core:home')
        return HttpResponse('already authenticated')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # authenticate user's, email and password
        if user is not None:
            login(request, user)
            return HttpResponse('signin')
            # return redirect('core:home')
        else:
            error = 'Invalid Username or Password'
            form = AuthenticationForm(request.POST)
            return render(request, 'account/login.html', {'form': form, 'error': error})
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('account:login')


def password_reset_request(request):  # password reset for loged-out user
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']  # get user entered email
            associated_users = User.objects.filter(Q(email=data))  # find associated user with that email
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/password/password_reset_email.txt"  # email body stored in txt file
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)  # All email data rendered as string
                    try:
                        send_mail(subject, email, 'panda.throwawayyy@gmail.com', [user.email],
                                  fail_silently=True)  # Send Email
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


@login_required
def change_password(request):  # change password for logged-in user
    message = ''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # converting password to hash
            message = 'Password changed successfully'
            return redirect('core:home')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/password/password_reset_confirm.html', {'form': form, 'message': message})


def email_message(request):  # Show a message after signup process, to check email for verification
    return render(request, 'account/email_message.html')
