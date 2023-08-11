from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("homepage/", views.homepage_view, name="homepage"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
]