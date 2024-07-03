import secrets
import string
import random

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения вашей почты перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class RestorePassword(TemplateView):
    template_name = 'users/password_reset_form.html'

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            user.set_password(password)
            user.save()
            send_mail(
                subject='Создание нового пароля',
                message=f'Ваш новый пароль: {password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            messages.success(self.request, 'Новый пароль отправлен на вашу почту.')
            return redirect(reverse('users:login'))
        else:
            messages.error(self.request, 'Пользователь с таким адресом электронной почты не найден.')
            return redirect(reverse('users:password_reset_form'))
