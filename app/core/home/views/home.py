from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = 'home/home.html'   

class ContactosView(TemplateView):
    template_name = 'home/contact.html'

class AboutView(TemplateView):
    template_name = 'home/about.html'
