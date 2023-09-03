from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'category']
    list_filter = ['category']
    list_display_links = ['title']

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Category)