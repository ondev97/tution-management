from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegsitrationForm,TeacherForm,AuthenticationForm,UserUpdateForm,StudentForm
from django.contrib import messages
from .models import Teacher

# Create your views here.
def home(request):
    user = request.user.username
    obj = Teacher.objects.filter(username = user)
    return render(request,'accounts/index.html',{"teachers":obj})

def register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Resgistration success")
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # account = authenticate(email=email,password=raw_password)
            # login(request,account)
            print("logged in")
        else:
            err = form.errors
            messages.error(request,err)

    return render(request,'accounts/form.html',{"form":TeacherForm()})

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("already logged in")

    if request.POST:
        form = AuthenticationForm(data=request.POST)
        print("form is POST")
        if form.is_valid():
            print("valid")
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                print("logged in")
                return redirect('accounts:home')
        else:
            err = form.errors
            messages.error(request,err)
            print("not logged in")

    else:
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{"form":AuthenticationForm()})


def logout_view(request):
    logout(request)
    return HttpResponse ("logged out")

def update_user(request,un):

    obj = Teacher.objects.get(username = un)
    print("object",obj.username)
    print("username",request.user.username)

    if request.user.username == obj.username:
        form = UserUpdateForm(instance=obj)
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                print("updated")

    else:
        return redirect('accounts:home')

    return render(request,'accounts/update.html',{"form":form})

def studentregister(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Resgistration success")
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # account = authenticate(email=email,password=raw_password)
            # login(request,account)
            print("logged in")
        else:
            err = form.errors
            messages.error(request,err)

    return render(request,'accounts/form.html',{"form":StudentForm()})