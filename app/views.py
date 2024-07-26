from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Donate

# Create your views here.
def index(request):
    register = Donate.objects.all()
    return render(request,'index.html', {'register' : register})

def donate(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')         
    else:
        form = RegisterForm()  
    return render(request,"donate.html", {'form' : form})

def details(request,id):
    r = Donate.objects.get(id=id)
    return render(request,'details.html', {'r' : r})

def update(request,id):
    r = Donate.objects.get(id=id)
    if request.method == 'POST' :
        form = RegisterForm(request.POST, request.FILES, instance=r)
        if form.is_valid():
            form.save() 
            return redirect('index')
    else:
        form = RegisterForm(instance=r)    
    return render(request,'update.html', {'form': form,'r' : r})

def delete(request,id):
    r = Donate.objects.get(id=id)
    r.delete()
    return redirect('index')      