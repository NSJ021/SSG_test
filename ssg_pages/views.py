from django.shortcuts import render
from .models import Team

# Create your views here.


def home(request):
    team = Team.objects.all()
    
    return render(request, 'ssg_pages/home.html', 
        {
            'team': team,  
        },
    )

def games(request):
    return render(request, 'ssg_pages/games.html')

def about(request):
    team = Team.objects.all()
    
    return render(request, 'ssg_pages/about.html', 
        {
            'team': team,  
        },
    )
    
def blog(request):
    return render(request, 'ssg_pages/blog.html')

def contact(request):
    return render(request, 'ssg_pages/contact.html')