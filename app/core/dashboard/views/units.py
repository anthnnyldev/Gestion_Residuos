from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.dashboard.models import Units
from core.dashboard.forms.unitsform import UnitsForm
from django.contrib.auth.mixins import LoginRequiredMixin

class UnitsListView(LoginRequiredMixin, ListView):
    model = Units
    template_name = 'core/dashboard/units/unit_list.html'
    context_object_name = 'units'
    
    def get_queryset(self):
        queryset = Units.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(description__icontains=query)
        return queryset

class UnitsCreateView(LoginRequiredMixin, CreateView):
    model = Units
    template_name = 'core/dashboard/units/unit_form.html'
    form_class = UnitsForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('dashboard:unit_list')

class UnitsUpdateView(LoginRequiredMixin, UpdateView):
    model = Units
    template_name = 'core/dashboard/units/unit_form.html'
    form_class = UnitsForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('dashboard:unit_list')

class UnitsDeleteView(LoginRequiredMixin, DeleteView):
    model = Units
    template_name = 'core/dashboard/units/unit_delete.html'
    
    success_url = reverse_lazy('dashboard:unit_list')