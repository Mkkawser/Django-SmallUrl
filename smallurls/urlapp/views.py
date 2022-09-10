from http.client import HTTPResponse
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate
from datetime import datetime
from urlapp.models import Url, guest


def HomePage(request):
    token = get_random_string(length=6)
    dic = {
        'data': Url.objects.filter(user_id=request.user.id),
        'token': token,
        'anonymous': guest.objects.last()
    }
    if request.method == 'POST':
        user = request.user
        urls = request.POST.get('urls')
        alias = request.POST.get('alias')
        date = datetime.now().strftime("%d %m %Y %I:%M %p")
        if user.is_authenticated:  # authorized
            root = Url(user=user, urls=urls, alias=alias,
                       date=date, token=token)
            root.save()
            return redirect(HomePage)
        else:  # Guest
            root = guest()
            root.urls = urls
            root.link = token
            root.uuid = token
            root.save()
            return redirect(HomePage)
    return render(request, 'home.html', dic)


def goto(request, token_id):
    dic = {}
    ob = None
    if request.user.is_authenticated:
        ob = Url.objects.get(token=token_id)
        return redirect(ob.urls)
    else:
        ob = guest.objects.get(uuid=token_id)
        dic['data'] = ob
        print(ob)
        return redirect(ob.urls)
    return render(request, 'goto.html', dic)


def accPage(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['pword']
        try:
            email = request.POST['email']  # Create Acc
            user = User.objects.create_user(
                username=uname, email=email, password=upass)
            user.save()
            login(request, user)
            return redirect('/')
        except:  # login
            root = authenticate(request, username=uname, password=upass)
            if root is not None:
                login(request, root)
                return redirect('/')
            else:
                return HTTPResponse('Invalid')
    return render(request, 'account.html')


def logout_page(request):  # logout
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    return render(request, 'home.html')
