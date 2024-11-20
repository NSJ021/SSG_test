from django.shortcuts import render, redirect

# Create your views here.

def signup(request):
    return render(request, 'ssg_accounts/signup.html')

def login(request):
    return render(request, 'ssg_accounts/login.html')

def logout(request):    
    return redirect('home')

def dashboard(request):
    return render(request, 'ssg_accounts/dashboard.html')