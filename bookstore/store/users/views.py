from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.models import User
from users.forms import UserLoginform, UserRegistrationForm, UserProfileForm

from products.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginform(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginform()
    context = {'form': form, 'title': 'Страница авторизации'}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('users:login'))
        else:
            pass
    else:
        form = UserRegistrationForm()
    
    context = {'form': form, 'title': 'Страница регистрации'}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm( instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)


    context = {
        'title': 'Store - Профиль', 
        'form': form,
        'baskets': Basket.objects.filter(user=request.user), 
        }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))