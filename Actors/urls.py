from django.contrib import admin
from django.urls import path
from .import views
from KoreanForum import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
urlpatterns = [
    path('a',views.actor,name='actor'),
    path('',views.base,name='base'),
    path('actors/detail/<str:menu>',views.detail,name='detail'),
    path('login',login,{'template_name' :'login.html'},name='login'),
    path('signup',views.register,name='signup'),
    path('author',views.author,name='author'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)