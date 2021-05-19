from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home-view'),
    path('about/', aboutView, name='about-view'),
    path('gallery/', galleryView, name='gallery-view'),
    path('blogs/', BlogView, name='blog-view'),
    path('contact/', contactView, name='contact-view'),
    path('category/<int:cid>/', ShowCatView, name='show-cat-view'),
    path('blogs/read/<int:blog_id>/', BlogRead, name='blog-read-view'),
    path('blogs/category/<int:cat_id>/', BlogCategory, name='blog-category-view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)