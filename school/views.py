from django.shortcuts import render,redirect,get_object_or_404
from .models import NewUser
from .forms import SignupForm, LoginForm
from django.http import HttpResponse
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
                     
                elif user.role == 'S':
                    messages.success(request, 'You are logged in as a student')
                                  
            else:
                messages.warning(request, 'Invalid details')

    return render(request, 'login.html', {'signin': signin_form})


def signout(request):
    logout(request)
    return HttpResponse('Successful logout')
def profile(request):
    return render(request,'profile.html')