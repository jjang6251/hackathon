from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import User
#프로필 수정 오버라이드
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm


from .forms import EditProfileForm

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

def find_id_view(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        ph_num = request.POST["ph_num"]

        try:
            user = User.objects.get(Q(first_name=firstname) & Q(last_name=lastname) & Q(ph_num=ph_num))
            print("회원정보 일치")
            messages.info(request, f"회원정보 일치 : 아이디는 {user.username} 입니다.")
        except User.DoesNotExist:
            print("회원정보 불일치")
            messages.error(request, "회원정보 불일치 : 해당 정보로 등록된 계정이 없습니다.")

    return render(request, "accounts/find_id.html")


def find_pw_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        ph_num = request.POST["ph_num"]
        resi_num = request.POST["resi_num"]

        try:
            user = User.objects.get(
                Q(first_name=first_name) & Q(last_name=last_name) &
                Q(ph_num=ph_num) & Q(resi_num=resi_num))
            print("회원정보일치")
            messages.info(request, "회원정보 일치 : 비밀번호 초기화를 진행합니다.")
            return render(request, "accounts/reset_pw.html")
        except User.DoesNotExist:
            print("회원정보불일치")
            messages.error(request, "회원정보 불일치 : 해당 정보로 등록된 계정이 없습니다.")

    return render(request, "accounts/find_pw.html")


def reset_pw_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            User = get_user_model()
            user = User.objects.get(username=username)
            try:
                user.set_password(password)
                user.save()
                messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
                return render(request, 'accounts/login.html')
            except User.DoesNotExist:
                messages.error(request, '사용자를 찾을 수 없습니다.')

    return render(request, 'accounts/find_id.html')
   

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

#프로필 수정 파트

def edit_profile(request):
    # 프로필 수정 템플릿을 렌더링합니다.
    return render(request, "accounts/profile/edit.html")

@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST.get("first_name", "")
        user.last_name = request.POST.get("last_name", "")
        user.email = request.POST.get("email", "")
        user.address = request.POST.get("address", "")
        user.ph_num = request.POST.get("ph_num", "")
        user.nickname = request.POST.get("nickname", "")
        user.save()
        return redirect("accounts:profile")
    return render(request, "accounts/edit_profile.html", {"user": user})

class EditProfileView(LoginRequiredMixin, FormView):
    template_name = 'accounts/edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('accounts:profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        initial['address'] = user.profile.address
        initial['ph_num'] = user.profile.ph_num
        initial['nickname'] = user.profile.nickname
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.profile.address = form.cleaned_data['address']
        user.profile.ph_num = form.cleaned_data['ph_num']
        user.profile.nickname = form.cleaned_data['nickname']
        user.save()

        profile = user.profile
        profile.phone_number = form.cleaned_data['phone_number']
        profile.website = form.cleaned_data['website']
        profile.save()

        return super().form_valid(form)
