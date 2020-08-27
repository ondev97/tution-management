from django.shortcuts import render, redirect
from .forms import CourseCreationForm,AddModule
from accounts.models import Teacher
from .models import Course, Module
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # print(Teacher.objects.get(username=request.user))
            print(request.user.username)
            instance.author = Teacher.objects.get(username=request.user.username)
            instance.save()
            print("saved")
        else:
            print('not saved')
    return render(request, 'course/course_create.html', {'form': CourseCreationForm()})


@login_required
def view_course(request):
    uid = request.user
    obj = Course.objects.filter(author=uid)
    modules = Module.objects.all()
    return render(request, 'course/courses.html', {"obj": obj, "mod": modules})


def delete_course(request, pk):
    user = request.user
    print(user)
    obj = Course.objects.filter(Q(author=user) & Q(id=pk))
    obj.delete()
    return redirect('course:list')

def single_course(request,pk):
    form = AddModule(request.POST)
    obj = Course.objects.get(id=pk)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course = obj
            instance.save()
            print("saved")
        else:
            print('not saved')

    return render(request,'course/single_course.html',{"course":obj,"form":form})


def course_display(request,cn):
    course = Course.objects.get(course_name = cn)
    print(course)
    modules = Module.objects.filter(course = course)
    return render(request,'course/course_unit.html',{"course":course,"module":modules})