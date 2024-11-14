from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = 'components/home.html'