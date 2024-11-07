from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'ssg_pages/home.html')

def games(request):
    return render(request, 'ssg_pages/games.html')

def about(request):
    return render(request, 'ssg_pages/about.html')

def blog(request):
    return render(request, 'ssg_pages/blog.html')

def contact(request):
    return render(request, 'ssg_pages/contact.html')