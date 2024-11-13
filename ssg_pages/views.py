from django.shortcuts import render
from .models import Team
from ssg_blog.models import Post, Comment
from ssg_games.models import Game


# Create your views here.


def home(request):
    team = Team.objects.all()
    post = Post.objects.all()
    comment = Comment.objects.all()
    game = Game.objects.all()
    
    return render(request, 'ssg_pages/home.html', 
        {
            'team': team,
            'posts': post,
            'comments': comment,
            'games': game 
        },
    )

def games(request):
    game = Game.objects.all()
    return render(request, 'ssg_games/games.html',
        {
            'games': game
        },
    )
                  

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