from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import os


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in ['.jpg', '.jpeg']:
        raise ValidationError("Solo se permiten imágenes con formato .jpg o .jpeg.")


class Units(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_units"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_units"
    )
    
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
    
    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_categories"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_categories"
    )
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', validators=[validate_image_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    units = models.ForeignKey(Units, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_products"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_products"
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_locations"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_locations"
    )

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'

    def __str__(self):
        return f"{self.name} - {self.city}"


class Points(models.Model):
    ACTION_CHOICES = [
        ('TASK_COMPLETED', 'Tarea Completada'),
        ('PRODUCT_REQUEST', 'Solicitud de Producto'),
        ('PURCHASE', 'Compra Realizada'),
        ('PENALTY', 'Penalización'),
    ]

    number = models.PositiveIntegerField()  # Puntos otorgados (pueden ser negativos también si es una penalización)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="points")
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_points"
    )

    class Meta:
        verbose_name = 'Punto'
        verbose_name_plural = 'Puntos'

    def __str__(self):
        return f"{self.number} puntos para {self.user} por {self.get_action_type_display()}"


class PointHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="point_history")
    points = models.PositiveIntegerField()
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_point_histories"
    )

    class Meta:
        verbose_name = 'Historial de Puntos'
        verbose_name_plural = 'Historial de Puntos'

    def __str__(self):
        return f"{self.points} puntos - {self.action}"


class ProductRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('APPROVED', 'Aprobada'),
        ('DENIED', 'Denegada'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="product_requests"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name="requests"
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='PENDING'
    )
    points_assigned = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="reviewed_requests"
    )

    class Meta:
        verbose_name = 'Solicitud de Producto'
        verbose_name_plural = 'Solicitudes de Producto'

    def __str__(self):
        return f"Solicitud de {self.user} para {self.product} - {self.get_status_display()}"

    def approve(self, admin_user, points):
        if points < 0:
            raise ValidationError("Los puntos no pueden ser negativos.")
        
        # Verificar si ya existen puntos asignados para la solicitud
        existing_points = Points.objects.filter(user=self.user, action_type='PRODUCT_REQUEST').first()
        if existing_points:
            # Si ya existe un registro de puntos, actualízalo en lugar de crear uno nuevo
            existing_points.number += points
            existing_points.save()
        else:
            # Si no existe, crea uno nuevo
            Points.objects.create(
                user=self.user,
                number=points,
                action_type='PRODUCT_REQUEST',
                created_by=admin_user
            )

        self.status = 'APPROVED'
        self.reviewed_by = admin_user
        self.points_assigned = points
        self.save()

        # Registrar el historial de puntos
        PointHistory.objects.create(
            user=self.user,
            points=points,
            action=f"Producto gestionado: {self.product.name}",
            created_by=admin_user
        )

    def deny(self, admin_user):
        self.status = 'DENIED'
        self.reviewed_by = admin_user
        self.save()

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points_required = models.PositiveIntegerField()
    image = models.ImageField(upload_to='rewards/')
    
    def __str__(self):
        return self.name