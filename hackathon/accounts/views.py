from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("accounts:login")

def signup_view(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        resi_num = request.POST["resi_num"]
        ph_num = request.POST["ph_num"]
        nickname = request.POST["nickname"]
        resi_img = request.FILES["resi_img"]
        present_img = request.FILES["present_img"]

        if password == password2:
            user =  User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.firstname = firstname
            user.gender = gender
            user.address = address
            user.gender = gender
            user.ph_num = ph_num
            user.resi_num = resi_num
            user.nickname = nickname
            user.resi_img = resi_img
            user.present_img = present_img
            user.save()
            return redirect("accounts:login")
        else:
            return redirect("accounts:signup")
        

        
    return render(request, "accounts/signup.html")

def homepage_view(request):
    return render(request, "accounts/homepage.html")