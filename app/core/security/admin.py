from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(FinalUser)
class FinalUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_admin_user')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_admin_user')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'created_at', 'updated_at')
    search_fields = ('description')


@admin.register(Unit)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('description',  'created_at', 'updated_at')
    search_fields = ('description')
    
@admin.register(Product)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('number', 'user', 'updated_at')
    search_fields = ('description')


@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('number', 'user', 'created_at')  
    search_fields = ('user__email',)
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name')