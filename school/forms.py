from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Yourname')
    class Meta:
        model = NewUser
        fields = ('username', 'first_name','last_name','email', 'reg_no','password1', 'password2','role')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = '__all__'
class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields= '__all__'
class AddStudentForm(forms.ModelForm):
    class Meta:
        model =NewUser
        fields = ('first_name','last_name','email')
           
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Enter your Username",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets={
        'username': forms.PasswordInput(attrs={'class': 'form-control form-label','placeholder':'Enter your username'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control form-label','placeholder':'Enter your password'}),
    }
