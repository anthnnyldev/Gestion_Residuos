from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(default=False, help_text="Indica si el usuario es un administrador.")
    phone_number = models.CharField(max_length=10, blank=True, help_text="Número de teléfono del usuario.")
    address = models.CharField(max_length=255, blank=True, help_text="Dirección del usuario.")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del usuario.")
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True, help_text="Género del usuario.")
    profile_image = models.ImageField(upload_to='profile_img/', null=True, blank=True, help_text="Imagen de perfil del usuario.")
    
    ROLE_CHOICES = [
        ('USER', 'Usuario'),
        ('ADMIN', 'Administrador'),
    ]
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='USER', help_text="Rol del usuario.")
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    @property
    def get_role(self):
        if self.is_superuser:
            return 'Superuser'
        return self.role

    @property
    def get_role_display(self):
        roles = {
            'Superuser': 'Super Administrador',
            'Admin': 'Administrador',
            'USER': 'Usuario'
        }
        return roles.get(self.get_role, 'Usuario')

    def __str__(self):
        return f"{self.username} ({self.get_role_display})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    groups = models.ManyToManyField(Group, related_name='security_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='security_user_set', blank=True)


@receiver(post_save, sender=User)
def assign_group_based_on_role(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            group, created = Group.objects.get_or_create(name='Superuser')
        elif instance.role == 'ADMIN':
            group, created = Group.objects.get_or_create(name='Admin')
        else:
            group, created = Group.objects.get_or_create(name='User')
        
        if not instance.groups.filter(name=group.name).exists():
            instance.groups.add(group)
