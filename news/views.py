from django.shortcuts import render, get_object_or_404
from .models import Post, Slider, Advertisement

def index(request):
    posts = Post.objects.all()
    sliders = Slider.objects.all()
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/index.html', {
        'posts': posts,
        'sliders': sliders,
        'breaking_news': breaking_news,
        'advertisement': advertisement
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()
    return render(request, 'pages/post_detail.html', {
        'post': post,
        'breaking_news': breaking_news,
        'advertisement': advertisement
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
