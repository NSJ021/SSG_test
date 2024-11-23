"""
This module contains the views for the application.

Views:
    home: Renders the home page with team members, posts, comments, and games.
    games: Renders a list of all the games in the database.
    about: Renders the about page with team members.
    blog: Renders the blog page with posts and comments.
    contact: Renders the contact page.
"""

from django.shortcuts import render
from ssg_blog.models import Post, Comment
from ssg_games.models import Game
from .models import Team


# Create your views here.

def home(request):
    """
    Renders the home page with team members, posts, comments, and games.

    **Context**

    ``team``
        A queryset of all team members.
    ``posts``
        A queryset of all blog posts.
    ``comments``
        A queryset of all comments.
    ``games``
        A queryset of all games.

    **Template:**

    :template:`ssg_pages/home.html`
    """
    # Fetch all team members, posts, comments, and games from the database
    team = Team.objects.all()
    post = Post.objects.all()
    comment = Comment.objects.all()
    game = Game.objects.all()
    # Render the home page template with the fetched data
    return render(request, 'ssg_pages/home.html',
        {
            'team': team,
            'posts': post,
            'comments': comment,
            'games': game 
        },
    )

def games(request):
    """
    Renders a list of all the games in the database.

    **Context**

    ``games``
        A queryset of all games.

    **Template:**

    :template:`ssg_games/games.html`
    """
    # Fetch all games from the database
    game = Game.objects.all()
    # Render the games page template with the fetched data
    return render(request, 'ssg_games/games.html',
        {
            'games': game
        },
    )
def about(request):
    """
    Renders the about page with team members.

    **Context**

    ``team``
        A queryset of all team members.

    **Template:**

    :template:`ssg_pages/about.html`
    """
    # Fetch all team members from the database
    team = Team.objects.all()
    # Render the about page template with the fetched data
    return render(request, 'ssg_pages/about.html',
        {
            'team': team,  
        },
    )
def blog(request):
    """
    Renders the blog page with posts and comments.

    **Context**

    ``posts``
        A queryset of all blog posts.
    ``comments``
        A queryset of all comments.

    **Template:**

    :template:`ssg_blog/blog.html`
    """
    # Fetch all blog posts and comments from the database
    post = Post.objects.all()
    comment = Comment.objects.all()
    # Render the blog page template with the fetched data
    return render(
        request, 'ssg_blog/blog.html',
            {
                'posts': post,
                'comments': comment
            },
    )

def contact(request):
    """
    Renders the contact page.

    **Template:**

    :template:`ssg_pages/contact.html`
    """
    # Render the contact page template
    return render(request, 'ssg_pages/contact.html')
