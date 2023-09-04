from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug>/', views.post_detail, name= 'post_detail'),
    path('soccer/', views.soccer, name='soccer'),
    path('basketball/', views.basketball, name='basketball'),
    path('volleyball/', views.volleyball, name='volleyball'),
    path('othersports/', views.othersports, name='othersports'),
    path('about-us/', views.about, name='aboutus'),
    path('contact-us/', views.contact, name='contactus'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)