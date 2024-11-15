from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from core.security.models import User
from core.security.forms.authform import RegisterForm, LoginForm

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'core/security/auth/register.html'
    success_url = reverse_lazy('security:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        messages.success(self.request, "¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.")
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al registrar la cuenta. Por favor, revisa los campos.")
        return super().form_invalid(form)

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'core/security/auth/login.html'
    success_url = reverse_lazy('dashboard:home')

    def form_valid(self, form):
        user = form.cleaned_data['user']

        if user.is_authenticated:
            login(self.request, user)
            messages.success(self.request, "¡Bienvenido de nuevo!")
            return redirect(self.success_url)
        
        messages.error(self.request, "Nombre de usuario o contraseña incorrectos.")
        return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Nombre de usuario o contraseña incorrectos.")
        return super().form_invalid(form)
    
def user_logout(request):
    logout(request)
    return redirect('security:login')
