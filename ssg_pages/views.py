from django.shortcuts import render
from .models import Team
from ssg_blog.models import Post, Comment


# Create your views here.


def home(request):
    team = Team.objects.all()
    
    return render(request, 'ssg_pages/home.html', 
        {
            'team': team,  
        },
    )

def games(request):
    return render(request, 'ssg_games/games.html')

def about(request):
    team = Team.objects.all()
    
    return render(request, 'ssg_pages/about.html', 
        {
            'team': team,  
        },
    )
    
def blog(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    return render(
        request, 'ssg_blog/blog.html',
            {
                'posts': post,
                'comments': comment
            },
   
            )

def contact(request):
    return render(request, 'ssg_pages/contact.html')