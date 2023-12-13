from django.shortcuts import render
from .forms import UserRegisterForm, UserLoginForm, TeacherRequest
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form
            user= user.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserRegisterForm() 
    return render(request,'registration/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = UserLoginForm()
        
    return render(request,'registration/login.html',{'form': form})

def rules(request):
    return render(request , 'rules.html')


def teacher_request(request):
    if request.method == 'POST':
        form = TeacherRequest(data=request.POST)
        instance = form.save(commit=False)
        instance.userinfo = request.user
        instance.save()
        return redirect('home')
        
    else:
        form = TeacherRequest()

    return render(request, 'accounts/request_teacher.html', {'form':form})



