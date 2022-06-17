#import email
#import re
#from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import studentRegistration
from firstapp.models import User

# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=studentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=studentRegistration()
    else:
        fm=studentRegistration() 
    stud=User.objects.all() 
    return render(request,'firstapp/Show.html', {'form':fm ,'stu':stud} ) 

def delete_data(request,id):
       if request.method=="POST":
           pi = User.objects.get(pk=id)
           pi.delete()
           return HttpResponseRedirect ('/firstapp/a1/')



def update_data(request,id):
    if request.method=="POST":
        x=User.objects.get(pk=id)
        fm=studentRegistration(request.POST,instance=x)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=studentRegistration(instance=pi)
    return render (request,'firstapp/update.html',{'form':fm})        
