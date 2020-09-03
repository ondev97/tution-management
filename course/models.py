from django.db import models
from accounts.models import Teacher,User,Student


# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=300,default=None)
    author = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,default=None)
    course_content = models.TextField(null=True)


    def __str__(self):
        return self.course_name


class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    module_name = models.CharField(max_length=100)
    module_content = models.CharField(max_length=100)


    def __str__(self):
        return self.module_name

class Enrollment(models.Model):
    name = models.CharField(max_length=100,default="Text here")
    course = models.ForeignKey(Course,models.CASCADE,null=True)
    student = models.ForeignKey(Student,models.CASCADE,null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['course','student']]





