from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from course.models import Course, Module
from accounts.models import Teacher
from django.http import JsonResponse

from course.api.serializers import CourseSerializer
from .serializers import CourseSerializer, ModuleSerializer


@api_view(['GET', ])
def courselist(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def coursemodule(request, cn):
    course = Course.objects.get(course_name=cn)
    module = Module.objects.filter(course=course)
    serializer = ModuleSerializer(module, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createcourse(request):
    user = request.user
    author = Teacher.objects.get(username=user.username)
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=author)
    return Response(serializer.data)
