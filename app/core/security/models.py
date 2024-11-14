from django.db import models
# Create your models here.

#2 model of user   final user  and admin user
# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Debe configurar email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class FinalUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin_user = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin_user = models.BooleanField(default=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Adminnistradores'



