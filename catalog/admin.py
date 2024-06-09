from django.contrib import admin
from catalog.models import Product, Category


# Register your models here.
# admin.site.register(Product)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','category_name', 'category_description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
