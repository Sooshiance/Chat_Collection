from django.shortcuts import render, redirect
from django.contrib import auth, messages

from .models import User
from .forms import Register


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('chat:home')
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, phone=phone, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'خوش آمدید')
            return redirect('chat:home')
        else:
            messages.error(request, 'مشخصات وارد شده اشتباه می باشد، دوباره تلاش کنید')
            return render(request, 'user/login.html')
    return render(request, "user/login.html")


def logoutUser(request):
    auth.logout(request)
    messages.info(request, 'به امید دیداری دوباره')
    return redirect('user:login')


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password, phone=phone)
            user.set_password(password)
            messages.success(request, 'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('chat:home')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('user:login')
    else:
        form = Register()
    return render(request, "user/signup.html", {'form': form})
