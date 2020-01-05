from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.template import RequestContext


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username, password = password)
            newUser.set_password(password)

            newUser.save()
            login(request, newUser)
            messages.info(request, "Your registration is successfull...")

            return redirect("index")

        context = {
            "form": form
        }
        return render(request, "register.html", context) 

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context)



def loginUser(request):
    form = LoginForm(request.POST or None)

    context= {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username, password= password)

        if user is None:
            messages.info(request, "Username or Password is wrong!")
            return render(request, "login.html", context)

        messages.success(request, "Welcome, " + username.capitalize())
        login(request, user)
        return redirect("index")


    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Successfull logout...")
    return redirect("index")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)            # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })                           


def change_username(request):

    if request.method == 'POST':
        
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user_save = form.save()
            update_session_auth_hash(request, user_save)            # Important!
            messages.success(request, 'Your username was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'change_username.html', {
        'form': form
    })


def Account(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)            # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account.html', {
        'form': form
    }) 




