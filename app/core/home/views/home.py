from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = 'home/home.html'

class NoticiasView(TemplateView):
    template_name = 'noticias.html'

class TutorialView(TemplateView):
    template_name = 'tutorial.html'

class SobreNosotrosView(TemplateView):
    template_name = 'sobre_nosotros.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'

class LoginView(TemplateView):
    template_name = 'login.html'