from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

class LoginView(TemplateView):
    template_name = 'core/security/login.html'

class RegisterView(TemplateView):
    template_name = 'core/security/register.html'