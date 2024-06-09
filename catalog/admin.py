from django.contrib import admin
from catalog.models import Product, Category
# Register your models here.
# admin.site.register(Product)

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','category', 'image', 'price', 'created_at', 'updated_at', 'manufactured_at')
    list_filter = ('category',)