from django.contrib import admin
from .models import Post, Category, Slider, Advertisement

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'category']
    list_filter = ['category']
    list_display_links = ['title']

    class Meta:
        model = Post

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'category']
    list_filter = ['category']
    list_display_links = ['title']

    class Meta:
        model = Slider

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    list_display_links = ['title']

    class Meta:
        model = Advertisement

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
