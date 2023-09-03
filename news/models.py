from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="null")
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'post'
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'
        ordering = ['-created_at']
