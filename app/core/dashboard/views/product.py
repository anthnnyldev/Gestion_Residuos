from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.dashboard.models import Product, Category, Units
from core.dashboard.forms.productform import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'core/dashboard/products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(description__icontains=query)
        return queryset

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'core/dashboard/products/product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['units'] = Units.objects.all()
        return context

    success_url = reverse_lazy('dashboard:product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'core/dashboard/products/product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['units'] = Units.objects.all()
        return context

    success_url = reverse_lazy('dashboard:product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'core/dashboard/products/product_delete.html'
    
    success_url = reverse_lazy('dashboard:product_list')

class ProductToggleStatusView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.is_active:
            product.hide()
            messages.success(request, f"Producto {product.description} ocultado.")
        else:
            product.show()
            messages.success(request, f"Producto {product.description} activado.")
        
        return redirect('dashboard:product_list')
