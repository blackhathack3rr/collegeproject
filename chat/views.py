from chat.models import ChatServer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from blog import models
# Create your views here.
@login_required
def host(request):
    form = ChatServer.objects.all()
    return render(request, 'chat.html', {'form': form})

@login_required
def sea(request):
    if request.method == "POST" :
        query = request.POST.get('usermsg')
        he = request.POST.get('use')
        ChatServer.objects.create(cuser_id=he,message=query)
        form = ChatServer.objects.all()
        return render(request, 'chat.html', {'form': form})
    form = ChatServer.objects.all()
    return render(request,'chat.html', {'form':form})
