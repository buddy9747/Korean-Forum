from django.shortcuts import render
from .models import dish,dishD
# Create your views here.
def food(request):
    a=dish.objects.all()
    return render(request,'Foods/food.html',{'a':a})

def food_detail(request):
    b=dishD.objects.all()
    return render(request,'Foods/food_detail.html',{'b':b})