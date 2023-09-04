from django.shortcuts import render, get_object_or_404
from .models import Post, Slider, Advertisement, Category

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

def soccer(request):
    category = Category.objects.get(category='Futbol')
    posts = Post.objects.filter(category=category)
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/soccer.html', {
        'posts': posts,
        'breaking_news': breaking_news,
        'advertisement': advertisement,
        'category': category
    })

def basketball(request):
    category = Category.objects.get(category='Basketbol')
    posts = Post.objects.filter(category=category)
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/basketball.html', {
        'posts': posts,
        'breaking_news': breaking_news,
        'advertisement': advertisement,
        'category': category
    })

def volleyball(request):
    category = Category.objects.get(category='Voleybol')
    posts = Post.objects.filter(category=category)
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/volleyball.html', {
        'posts': posts,
        'breaking_news': breaking_news,
        'advertisement': advertisement,
        'category': category
    })

def othersports(request):
    category = Category.objects.get(category='Diğer Sporlar')
    posts = Post.objects.filter(category=category)
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/othersports.html', {
        'posts': posts,
        'breaking_news': breaking_news,
        'advertisement': advertisement,
        'category': category
    })

def about(request):
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/about-us.html', {
        'breaking_news': breaking_news,
        'advertisement': advertisement
    })

def contact(request):
    breaking_news = list(Post.objects.order_by('-created_at')[:5])
    advertisement = Advertisement.objects.all()

    return render(request, 'pages/contact-us.html', {
        'breaking_news': breaking_news,
        'advertisement': advertisement
    })
