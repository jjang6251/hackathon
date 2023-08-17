from django.urls import path, include, reverse_lazy
from . import views
from .views import profile_view, edit_profile_view


app_name = "accounts"

urlpatterns = [
    path("homepage/", views.homepage_view, name="homepage"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("afterlogin/", views.after_login_view, name="afterlogin"),
    path("board/", include("board.urls")),
    path("profile/", views.profile_view, name="profile"),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
]