from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from django.db.models import Q

class ClientListView(ListView):
    model = get_user_model()
    template_name = 'core/security/client/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10  # Puedes ajustar el número de clientes por página

    def get_queryset(self):
        # Filtra usuarios con rol 'USER' y 'Superuser'
        return get_user_model().objects.filter(Q(role='USER') | Q(is_superuser=True))  # Filtra usuarios y superusuarios

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')

        user = get_user_model().objects.get(id=user_id)
        if action == 'assign_admin':
            # Asignar rol de administrador
            user.is_admin = True
            user.save()
            group, created = Group.objects.get_or_create(name='Admin')
            user.groups.add(group)
        elif action == 'remove_admin':
            # Remover rol de administrador
            user.is_admin = False
            user.save()
            group = Group.objects.get(name='Admin')
            user.groups.remove(group)
        return redirect(reverse('security:client_list'))
    

