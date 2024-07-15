from django.shortcuts import render

from blog.models import Blog
from django import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from pytils.translit import slugify
from django.core.mail import send_mail
from blog.forms import BlogForm

class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Список блогов'}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)

        return queryset


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blogs')
    extra_context = {'title': 'Добавление блога'}

    def form_valid(self, form):
        new_blog = form.save()
        new_blog.slug = slugify(new_blog.header)
        new_blog.save()

        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog
    fields = '__all__'
    extra_context = {'title': 'Блог'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            subject = f'{self.object.header} - очень популярный блог'
            message = f'Количество просмотров блога {self.object.header} превысило 100'
            from_email = 'djangopost@yandex.ru'
            recipient_list = ['avgl@mail.ru']
            send_mail(subject, message, from_email, recipient_list,fail_silently=False)

        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    success_url = reverse_lazy('blog:blogs')
    extra_context = {'title': 'Изменение блога'}

    def form_valid(self, form):
        new_blog = form.save()
        new_blog.slug = slugify(new_blog.header)
        new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs')
    extra_context = {'title': 'Удаление блога'}


