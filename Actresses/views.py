from django.shortcuts import render
from .models import Actres,ActresD

# Create your views here.
def actress(request):
    a=Actres.objects.all()
    return render(request,'Actresses/actress.html',{'a':a})

def actress_detail(request):
    b=ActresD.objects.all()
    return render(request,'Actresses/actress_detail.html',{'b':b})