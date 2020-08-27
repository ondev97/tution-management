from django import forms
from .models import Course,Module

class CourseCreationForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('course_name','course_content',)

class AddModule(forms.ModelForm):

    class Meta:
        model = Module
        fields = ('module_name','module_content',)

