from django.contrib import admin
from catalog.models import Product, Category, Contact, Blog


# Register your models here.
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','category_name', 'category_description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'phone', 'email')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk','header', 'slug', 'published')