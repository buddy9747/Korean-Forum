from django.shortcuts import render,redirect
from .models import ActD,Actors
from .forms import CustomUserCreationForm
from django.contrib import messages
import random
from django.views.generic import DetailView

# Create your views here.
def actor(request):
    a=Actors.objects.all()
    return render(request,'Actors/HomeAct.html',{'a': a})

'''def detail(request):
    b=ActD.objects.filter(act_id=7)
    return render(request,'Actors/ActPage.html',{'b': b})'''



a=[1,2,3,4,5,7,8,9,10,11]
def detail(request,menu):
    ac=Actors.objects.get(act_name=menu)
    ad=ActD.objects.get(act_id=ac)
    b=[]
    try:
        for i in range(0,3):
            b.append(Actors.objects.get(id=random.choice(a)))
    except ValueError():
        print("data not found")
    return render(request,'Actors/ActPage.html',{'object':ad,'b':b})

def base(request):
    return render(request,'base.html')

def author(request):
    return render(request,'author.html')


def register(request):
    if (request.method=='POST'):
        form =CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            user=form.save()
            user.refresh_from_db()
            user.employee.desig=form.cleaned_data['desig']
            user.save()
            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form= CustomUserCreationForm()

    args={'form':form}
    return render(request,'signup.html',args)