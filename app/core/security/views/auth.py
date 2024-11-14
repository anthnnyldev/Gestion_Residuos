from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

class LoginView(FormView):
    template_name = 'core/security/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home:home')  # Change 'home' to the URL name of your homepage or dashboard

    def form_valid(self, form):
        # Authenticate and log the user in
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Has iniciado sesión con éxito.")
            return super().form_valid(form)
        else:
            form.add_error(None, "El nombre de usuario o la contraseña no son correctos.")
            return self.form_invalid(form)

class RegisterView(FormView):
    template_name = 'core/security/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('security:login')  # Redirect to login page after successful registration

    def form_valid(self, form):
        # Create the user
        user = form.save(commit=False)
        user.first_name = self.request.POST.get('first_name', '')
        user.last_name = self.request.POST.get('last_name', '')
        user.email = self.request.POST.get('email', '')
        user.save()

        messages.success(self.request, "Cuenta creada exitosamente. Ahora puedes iniciar sesión.")
        return super().form_valid(form)
