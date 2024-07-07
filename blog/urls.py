from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import  BlogListView, BlogCreateView,BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('blog_form', BlogCreateView.as_view(), name='create'),
    path('blog_form/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='confirm_delete'),
]
