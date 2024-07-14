import secrets
import string

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User



# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject='Подтверждение почты',
                  message=f'Пожалуйста подтверди корректность почтового адреаса {url}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email]
                  )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ResetPasswordView(TemplateView):
    def get(self, request):
        return render(request, 'users/pass_reset.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            email = request.POST.get('email')

            new_pass = ''.join(
                secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10))
            user = User.objects.get(email=email)
            user.password = make_password(new_pass, salt=None, hasher='default')
            user.save()
            send_mail(
                subject='Новый пароль',
                message=f'Ваш новый пароль: {new_pass}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
        return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
