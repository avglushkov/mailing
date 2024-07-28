from django.urls import path, include
from django.views.decorators.cache import cache_page
from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView, ContactCreateView, ProductCreateView, ProductUpdateView, CategoryListView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),

]
