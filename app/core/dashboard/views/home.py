from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden
from core.dashboard.models import Product, ProductRequest

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
    
class ProductRequestCreateView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'core/request/request.html', {'product': product})

    def post(self, request, product_id):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("No tienes permiso para realizar esta acción.")

        product = get_object_or_404(Product, id=product_id)

        ProductRequest.objects.create(
            user=request.user,
            product=product,
            status='Pendiente',
        )

        messages.success(request, f'Solicitud para el producto {product.name} creada correctamente.')
        return redirect('dashboard:product_view')