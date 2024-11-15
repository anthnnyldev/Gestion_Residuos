from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import os

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in ['.jpg', '.jpeg']:
        raise ValidationError("Solo se permiten imágenes con formato .jpg o .jpeg.")

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(default=False, help_text="Indica si el usuario es un administrador.")
    phone_number = models.CharField(max_length=10, blank=True, help_text="Número de teléfono del usuario.")
    address = models.CharField(max_length=255, blank=True, help_text="Dirección del usuario.")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del usuario.")
    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        blank=True,
        help_text="Género del usuario."
    )
    profile_image = models.ImageField(
        upload_to='profile_img/', 
        null=True, 
        blank=True, 
        help_text="Imagen de perfil del usuario.",
        validators=[validate_image_extension]
    )
    
    ROLE_CHOICES = [
        ('USER', 'Usuario'),
        ('ADMIN', 'Administrador'),
    ]
    role = models.CharField(
        max_length=6,
        choices=ROLE_CHOICES,
        default='USER',
        help_text="Rol del usuario."
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    @property
    def get_role(self):
        if self.is_superuser:
            return 'Superuser'
        return self.role

    @property
    def get_role_display(self):
        return dict(self.ROLE_CHOICES).get(self.role, 'Usuario')

    def __str__(self):
        return f"{self.username} ({self.get_role_display})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    groups = models.ManyToManyField(Group, related_name='security_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='security_user_set', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group_name = 'Superuser' if self.is_superuser else dict(self.ROLE_CHOICES).get(self.role, 'User')
        group, created = Group.objects.get_or_create(name=group_name)
        if not self.groups.filter(name=group.name).exists():
            self.groups.add(group)


@receiver(post_save, sender=User)
def assign_group_based_on_role(sender, instance, created, **kwargs):
    if created:
        instance.save()
