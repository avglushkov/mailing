from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView, ContactCreateView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('blog/blog_form', BlogCreateView.as_view(), name='blog_form'),
    path('blog/blog_form/<int:pk>', BlogUpdateView.as_view(), name='blog_form'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_confirm_delete'),
]
