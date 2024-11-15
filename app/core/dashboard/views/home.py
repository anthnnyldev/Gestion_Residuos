from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from core.dashboard.models import Product

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard/home.html'
    login_url = '/security/auth/login'

class ProductView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard/product.html'
    login_url = '/security/auth/login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context