import secrets
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm
from users.models import CustomUser


class UserLoginView(LoginView):
    """ """
    template_name = "users/registration/login.html"
    success_url = reverse_lazy("catalog:home")


class UserLogoutView(LogoutView):
    """ """
    template_name = "users/registration/logout.html"
    next_page = reverse_lazy("catalog:home")


class RegisterView(CreateView):
    """ """
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:user_login")

    def form_valid(self, form):
        """ """
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    """ """
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:user_login"))