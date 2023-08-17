from django.urls import path, include
from . import views
from .views import profile_view, edit_profile_view


app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("afterlogin/", views.after_login_view, name="afterlogin"),
    path("board/", include("board.urls")),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile_view, name='edit_profile_view'),
    path("find_id/", views.find_id_view, name="find_id"),
    path("find_pw/", views.find_pw_view, name="find_pw"),
    path("reset_pw/", views.reset_pw_view, name="reset_pw"),
]