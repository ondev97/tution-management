from django.shortcuts import render, redirect,get_object_or_404
from .forms import CourseCreationForm,AddModule,EnrollmentForm,Enrollment
from accounts.models import Teacher,Student
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

def course_enroll(request,pk):
    objects = Course.objects.get(id=pk)
    form = EnrollmentForm(instance=objects)
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            student = Student.objects.get(username = request.user.username)
            instance.name = objects.course_name
            instance.course = objects
            instance.student = student
            instance.save()
            print("saved")
        else:
            print('not saved')
    return render(request,'course/enroll.html',{"form":form})

def stucourselist(request):
    objects = Course.objects.all()
    return render(request,'course/list.html',{'courses':objects})

def enrolled(request):
    obj = Enrollment.objects.filter(student = request.user)
    return render(request,'course/enrolled.html',{'courses':obj})