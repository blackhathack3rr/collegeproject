from django.http import HttpResponseRedirect
from django.shortcuts import render
from business.templates import *
from business.forms import *
# Create your views here.
def business(request):
    form=BusinessForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/home/")
    else:
        return render(request,"blogin.html",{'form':form})


def adds(request):
    form=AddsForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/home/")
    else:
        return render(request,"landing.html",{'form':form})

def login(request):
    if request.method=='POST':
        user=request.POST.get('username')
        pas=request.POST.get('password')
        rest=Business.objects.all()
        if(user):
            for i in rest:
                    if i.buser==user and i.pas==pas:
                        return HttpResponseRedirect("http://127.0.0.1:8000/adds/")

        else:
            return render(request, "actlogin.html")

    else:
        return render(request, "actlogin.html")