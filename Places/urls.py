from django.contrib import admin
from django.urls import path
from .import views
from KoreanForum import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
urlpatterns = [
    path('places',views.place,name='place'),
    path('place/detail',views.place_detail,name='place_detail')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)