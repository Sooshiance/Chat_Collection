from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from .models import Room
from .forms import RegisterRoom


def home(request):
    return render(request, "chat/index.html")


def allHall(request):
    r = Room.objects.all()
    return render(request, 'chat/allHall.html', {'rooms':r})


def chatPage(request, pk, *args, **kwargs):
    room_name = Room.objects.get(pk=pk)
    if not request.user.is_authenticated:
        return redirect("user:login")
    context = {'room_name': room_name}
    return render(request, "chat/chatPage.html", context)


def createRoom(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            form = RegisterRoom(request.POST)
            if form.is_valid():
                form.save()
                return redirect('chat:room')
            else:
                return redirect('chat:create-room')
        else:
            return HttpResponseNotAllowed("""You don't have permission to access this page""")
    else:
        return redirect('user:login')
