from django.db import models

class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(blank=True, null=True, max_length=100, verbose_name='Ссылка')
    content = models.TextField(blank=True, null=True, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    published = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Счетчик просмотров')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.header}'
# Create your models here.
