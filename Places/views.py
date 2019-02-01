from django.shortcuts import render
from .models import PlaceD,Place
# Create your views here.
def place(request):
    a=Place.objects.all()
    return render(request,'Places/place.html',{'a':a})

def place_detail(request):
    b=PlaceD.objects.all()
    return render(request,'Places/place_detail.html',{'b',b})