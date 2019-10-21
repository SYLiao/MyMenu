from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import userProfile
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import formLogin, formRegister
from django.utils import timezone

# Create your views here.

def register(request):

    if request.method == 'POST':

        form = formRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            cellphone = form.cleaned_data['cellphone']
            password = form.cleaned_data['password1']

            usernameCheck = auth.authenticate(username=username)

            if usernameCheck != None:
                return render(request, reverse('register'), {'form': form, 'message': 'Your username is existing.'})

            Userinstance = User.objects.create_user(username=username, password=password)

            userinstance = userProfile(user=Userinstance, username=username, cellPhoneNumber=cellphone, modifyDate=timezone.now())
            userinstance.save()

            return HttpResponseRedirect(reverse('login'))
        else:
            raise Exception('form is not vaild')

    else:
        form = formRegister()

    return render(request, 'register.html', {'form' : form})

def login(request):

    if request.method == 'POST':
        form = formLogin(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            ident = auth.authenticate(username=username, password=password)

            if ident != None and ident.is_active:
                auth.login(request, ident)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'login.html', {'form':form, 'message':'Your username or password is not correct.'})

    else:
        form = formLogin()

    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request, pk):
    Profile = userProfile.objects.filter(user=request.user).values()[0]
    print(reverse('profile', kwargs={'pk': pk}))
    return render(request, 'profile.html', {'username': Profile['username'],
                                                'cellPhoneNumber': Profile['cellPhoneNumber'],
                                                'modifyDate': Profile['modifyDate'],})