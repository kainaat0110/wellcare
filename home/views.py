from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index9(request):
    return render(request, "games.html")
def index2(request):
    return render(request, "login.html")
def index3(request):
    return render(request, "add.html")
def index4(request):
    return render(request, "diary.html")
def index5(request):
    return render(request, "comm.html")
def index6(request):
    return render(request, "sos.html")
def index7(request):
    return render(request, "afterlogin.html")
def index8(request):
    return render(request, "therapist.html")


def login1(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST.get('txt')
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            Cpassword = request.POST.get('Cpswd')
            if password != Cpassword:
                messages.warning(request,"Password Doesn't Match !!!")
                return redirect('login')
            else :
                try:
                    validate_email(email)
                    print("Email is valid")
                except ValidationError:
                    print("Email is invalid")
                my_user = User.objects.create_user(username,email,password)
                my_user.save()
                return redirect('login')

        # Handle login form submission
        elif 'login' in request.POST:
            username1 = request.POST.get('username')
            password1 = request.POST.get('pass')
            print(username1)
            print(password1)
            user = authenticate(request,username=username1,password=password1)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('afterlogin')
            else:
                return redirect('login')

    else:
        return render(request, 'login.html')
