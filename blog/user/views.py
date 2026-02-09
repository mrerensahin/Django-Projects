from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages




def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request, newUser)
            messages.success(request, "Başarıyla Kayıt oldunuz.")
            return redirect("index")
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    return render(request, "register.html", context)


def user_login(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form": form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request, "Kullanıcı Adı ve ya Parola Hatalıdır.")
            return render(request,"login.html", context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız..")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)

def user_logout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yapıldı.")
    return redirect("index")




    



    


    
