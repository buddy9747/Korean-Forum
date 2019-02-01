from django.contrib import admin
from django.urls import path
from .import views
from KoreanForum import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from .models import Actres,ActresD
urlpatterns = [
    path('actress',views.actress,name='actress'),
    path('actrees/detail',views.actress_detail,name='actress_detail')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)