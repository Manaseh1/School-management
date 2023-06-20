from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def register(request):
    signup = SignupForm()
    if request.method =="POST":
        if request.POST['password1'] != request.POST['password2']:
            messages.warning(request,'Passwords do not match')
        if NewUser.objects.filter(username=request.POST['username']):
            messages.info(request,'User already exists')
        if NewUser.objects.filter(email=request.POST['email']):
            messages.info(request,'Email already exists')
            return redirect('signup')
        signup = SignupForm(request.POST)
        if signup.is_valid():
            signup.save()
            messages.success(request,'Signup successful please login')
        # 
    return render(request,'signup.html',{'signup':signup})
# Create your views here.
def signin(request):
    signin_form = LoginForm()
   
    if request.method == "POST":
        signin_form = LoginForm(request.POST)
    
        if signin_form.is_valid():
            username = signin_form.cleaned_data.get('username')
            password = signin_form.cleaned_data.get('password') 
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                if user.role == 'A':
                    messages.success(request, 'You are logged in as an admin')
                    return  redirect('profile') 
                elif user.role == 'S':
                    messages.success(request, 'You are logged in as a student')
                    return  redirect('profile') 

            else:
                messages.warning(request, 'Invalid details')

    return render(request, 'login.html', {'signin': signin_form})

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    return render(request,'profile.html')

def example(request):
    allUsers = NewUser.objects.filter(Q(first_name__startswith='Man') | Q(last_name__startswith='Kel'))
    school =  School.objects.all()
    details = Course.objects.all()
    units = Units.objects.all()

    print(units)
    context = {
        'allUsers': allUsers,
        'details': details,
        'school': school,
        'units': units  
        }
    print(allUsers)
    print(details)
    return render(request,'output.html',context)
def CourseRegisters(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        user = request.user
        new_reg = CourseRegistration(user = user, chosen_course = course)
        new_reg.save()
    return render(request,'output.html')
@login_required
def AddCourse(request):
    form = AddCourseForm()
    if request.method == 'POST':
        form=AddCourseForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'AddCourse.html',{'form':form})

@login_required
def AddSchool(request):
    form = AddSchoolForm()
    if request.method == 'POST':
        form=AddSchoolForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'AddSchool.html',{'form':form})
@login_required
def AddStudent(request):
    form = AddStudentForm()
    if request.method == 'POST':
        form=AddStudentForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'AddStudent.html',{'form':form})