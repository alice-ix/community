from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import AliceUser
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form}) 


def register(request):
    
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        userName = request.POST.get('userName', None)
        userEmail = request.POST.get('userEmail', None)
        passWord = request.POST.get('passWord', None)
        re_passWord = request.POST.get('re-passWord', None)

        res_data = {}
        if not (userName and userEmail and passWord and re_passWord):
            res_data['error'] = '모든 칸의 정보를 입력해 주세요!!'
        elif passWord != re_passWord:
            res_data['error'] = '비밀번호를 다시 확인해 주세요'
        else:
            aliceUser = AliceUser(
            userName = userName,
            userEmail = userEmail,
            passWord = make_password(passWord)
            )
            aliceUser.save()

        return render(request, 'register.html', res_data)