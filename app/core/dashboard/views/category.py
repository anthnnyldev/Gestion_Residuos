from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.dashboard.models import Category
from core.dashboard.forms.categoryform import CategoryForm

class CategoryListView(ListView):
    model = Category
    template_name = 'core/dashboard/category/category_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        queryset = Category.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'core/dashboard/category/category_form.html'
    form_class = CategoryForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('dashboard:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'core/dashboard/category/category_form.html'
    form_class = CategoryForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('dashboard:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'core/dashboard/category/category_delete.html'
    
    success_url = reverse_lazy('dashboard:category_list')
