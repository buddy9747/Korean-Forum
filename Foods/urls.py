from django.contrib import admin
from django.urls import path
from .import views
from KoreanForum import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
urlpatterns = [
    path('dishes',views.food,name='food'),
    path('dish/detail',views.food_detail,name='food_detail')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)