from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description', 'category')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'slug', 'description', 'price', 'image')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'fields': ('category', 'stock', 'created_at', 'updated_at')
        }),
    )
