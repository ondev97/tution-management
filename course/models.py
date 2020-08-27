from django.db import models
from accounts.models import Teacher,User


# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=300)
    author = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    course_content = models.TextField(null=True)

    def __str__(self):
        return self.course_name


class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    module_name = models.CharField(max_length=100)
    module_content = models.CharField(max_length=100)

    def __str__(self):
        return self.module_name







