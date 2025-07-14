from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserLoginView, UserLogoutView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="user_login"),
    path(
        "logout/", UserLogoutView.as_view(next_page="catalog:home"), name="user_logout"
    ),
    path("register/", RegisterView.as_view(), name="user_register"),
    path("email_confirm/<str:token>/", email_verification, name="email_confirm"),
]
