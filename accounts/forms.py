from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Teacher
from django.contrib.auth import authenticate



class RegsitrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Error", error_messages={'required':"Email required"})

    class Meta:
        model = User
        fields = ('email','username','password1','password2')



class TeacherForm(UserCreationForm):

    class Meta:
        model = Teacher
        fields = ('email','username','password1','password2','full_name','subject',)


class AuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(username=email,password=password):
            raise forms.ValidationError("invalid login")


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('username','email','full_name','address','subject')