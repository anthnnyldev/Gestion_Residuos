from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden
from core.dashboard.models import Product, ProductRequest, Reward

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard/home.html'
    login_url = '/security/auth/login'

class RewardListView(ListView):
    model = Reward
    template_name = 'core/dashboard/rewards/rewards.html'
    context_object_name = 'rewards'

    def get_queryset(self):
        return Reward.objects.all()
    
class RewardCreateView(CreateView):
    model = Reward
    template_name = 'core/dashboard/rewards/reward_form.html'
    fields = ['name', 'description', 'points_required', 'image']
    success_url = reverse_lazy('dashboard:rewards_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
class RewardUpdateView(UpdateView):
    model = Reward
    template_name = 'core/dashboard/rewards/reward_form.html'
    fields = ['name', 'description', 'points_required', 'image']
    context_object_name = 'reward'
    success_url = reverse_lazy('dashboard:rewards_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
class RewardDeleteView(DeleteView):
    model = Reward
    template_name = 'core/dashboard/rewards/reward_delete.html'
    context_object_name = 'reward'
    success_url = reverse_lazy('dashboard:rewards_list') 

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