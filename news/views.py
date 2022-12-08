from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy


# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})

def dashboard_view(request):
    return render(request, 'dashboard.html' )

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')


'''def sign_up_view(request):
    if response.method == 'POST':
        form = UserCreationForm('response.POST')
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(response, 'register.html', {"form": form})'''
   
    
'''def sign_up_view(request):
    if request.method == 'POST':
        email      = request.POST['email']
        username   = request.POST['username']
        firstname  = request.POST['firstname']
        lastname   = request.POST['lastname']
        date       = request.POST['date']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        
        if password1 == passowrd2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username, password=password1,
                    email=email, firstname=firstanme, 
                    lastname=lastname
                 )
                user.save()
                print('user created')
                return redirect('/dashboard/')

        else:
            print('password not matching...')
            return redirect('register')

    else:
        return render(request, 'register.html')'''
    

'''def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #Redirect to a success page
            redirect('/dashboard')
        else:
            #Return an 'invalid login' error message
            messages.info(request, 'invalid credentials')
            form = AuthenticationForm()
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')'''

'''def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            authenticate(user)
            return redirect('/')
        else:
            messages.info(request, 'invalid login details')
            return redirect('/dashboard/')
    else:
        return render(request, 'login.html')'''


'''def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=username)

            if user:
                login(request, user)
                return redirect('dashboard')

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'login.html', context)'''

      