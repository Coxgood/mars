from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_page(request):
    return render(request, 'register/login_page.html')

def reg_page(request):
    args = {}
    args['form'] = UserCreationForm()
    return render(request, 'register/reg_page.html', context={'form': args['form']})

def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'],
                                        password = newuser_form.cleaned_data['password2'],
                                        )
            auth.login(request, newuser)
            return redirect('home')
        else:
            args['form'] = newuser_form
            mess = 'ошибка'
    return render(request, 'register/reg_page.html', context={'form': args['form'], 'mess': mess })

def login(request):
    args={}
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login error'] = "ошибка"
            return render(request, 'register/login_page.html', context={'args': args['login error']})
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect("/")