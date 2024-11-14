from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
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
    
class Points(models.Model):
    number = models.PositiveIntegerField()
    user = models.ForeignKey('FinalUser', on_delete=models.CASCADE, related_name="points")
    created_at= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Punto'
        verbose_name_plural = 'Puntos'
    
    def __str__(self):
        return f"{self.number} puntos"

class FinalUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin_user = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='security_finaluser_set', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='security_finaluser_permissions', blank=True
    )
    
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin_user = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='security_adminuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='security_adminuser_permissions', blank=True
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        

class Units(models.Model):
    description = models.CharField("Nombre de unidad", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
    
    def __str__(self):
        return f"{self.description}, {self.created_at} {self.updated_at}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return f"{self.name}, {self.created_at}, {self.updated_at}"


class Product(models.Model):
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    units = models.ForeignKey(Units, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return f"{self.description}, {self.image} {self.created_at}, {self.updated_at}"
