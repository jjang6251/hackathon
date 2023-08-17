from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import User,Profile
from .forms import EditProfileForm,ProfileForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
#프로필 수정 오버라이드

# from django.views.generic.edit import FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy

# from .forms import EditProfileForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return render(request, "accounts/afterlogin.html")
        else:
            print("인증실패")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("accounts:homepage")

def signup_view(request):
    
    if request.method == "POST":


        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        address_si = request.POST["address_si"]
        address_gu = request.POST["address_gu"]
        address_dong = request.POST["address_dong"]
        resi_num = request.POST["resi_num"]
        ph_num = request.POST["ph_num"]
        nickname = request.POST["nickname"]
        resi_img = request.FILES["resi_img"]
        present_img = request.FILES["present_img"]



        if password == password2:
            user =  User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            user.gender = gender
            user.address_si = address_si
            user.address_gu = address_gu
            user.address_dong = address_dong
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

def after_login_view(request):
    return render(request, "accounts/afterlogin.html")

#프로필 파트

def profile(request):
    # 프로필 템플릿을 렌더링합니다.
    
    return render(request, "accounts/profile.html")

@login_required
def profile_info(request):
    user = request.user
    # 유저의 정보를 처리하여 profile_info.html에 전달
    context = {
       'user': user,
     }
    return render(request, "accounts/profile_info.html", context)

def profile_view(request):
    user = request.user
    context = {
        # 템플릿에서 사용할 변수 값들
        'user': user,
        'profile_info': profile_info,
     }
    return render(request, "accounts/profile_info.html", {"user": user})

def profile(request):
    if request.method =='POST':
        user_change_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid()and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            return redirect('User',user.username)
        return redirect('accounts:profile')
    else: 
        user_change_form=EditProfileForm(instance=request.user)
        profile, create= Profile.objects.get_or_create(user=request.user)

    profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html',{
        'user_change_form':user_change_form,
        'profile_form':profile_form
    })




def edit_profile_view(request):
    #  프로필 수정 템플릿을 렌더링합니다.
    return render(request, "accounts/edit_profile.html")

# def edit_profile_view(request, id=None):
#     if id is None:
#         id = request.user.id
#     user = get_object_or_404(User, id=id)


#     if request.method == "POST":
#         user.first_name = request.POST.get("first_name", "")
#         user.last_name = request.POST.get("last_name", "")
#         user.email = request.POST.get("email", "")
#         user.address = request.POST.get("address", "")
#         user.ph_num = request.POST.get("ph_num", "")
#         user.nickname = request.POST.get("nickname", "")
#         user.save()
#         return redirect("accounts:profile")
#     return render(request, 'accounts/edit_profile.html', {'user': user})