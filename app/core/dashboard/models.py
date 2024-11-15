from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Units(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_units")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_units")
    
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
    
    def __str__(self):
        return f"{self.description}, {self.created_at} {self.updated_at}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop('user', None)
        self.updated_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_categories")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_categories")
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop('user', None)
        self.updated_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    units = models.ForeignKey(Units, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_products")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_products")

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return f"{self.description}, {self.image} {self.created_at}, {self.updated_at}"

    def hide(self):
        self.is_active = False
        self.save()

    def show(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop('user', None)
        self.updated_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_locations")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_locations")

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'

    def __str__(self):
        return f"{self.name}, {self.address}, {self.city}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop('user', None)
        self.updated_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)


class Points(models.Model):
    number = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="points")
    created_at= models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_points")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_points")

    class Meta:
        verbose_name = 'Punto'
        verbose_name_plural = 'Puntos'

    def clean(self):
        if self.number < 0:
            raise ValidationError("El número de puntos no puede ser negativo.")
    
    def __str__(self):
        return f"{self.number} puntos para {self.user}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop('user', None)
        self.updated_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)


class PointHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="point_history")
    points = models.PositiveIntegerField()
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_point_histories")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_point_histories")

    class Meta:
        verbose_name = 'Historial de Puntos'
        verbose_name_plural = 'Historial de Puntos'

    def __str__(self):
        return f"{self.points} puntos para {self.user} - {self.action}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = kwargs.pop('user', None)
        self.updated_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)
