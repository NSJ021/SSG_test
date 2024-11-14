"""
This module contains the views for the game application.

Views:
    Games: Renders a list of all the games in the database.
    game_detail: Displays an individual game entry.
"""

from django.shortcuts import render, get_object_or_404  # Import render and get_object_or_404 for rendering templates and fetching objects
from django.views import generic  # Import generic views for class-based views
from ssg_games.models import Game  # Import the Game model

# Create your views here.

class Games(generic.ListView):
    """
    Renders a list of all the games in the database.

    Attributes:
        queryset (QuerySet): The queryset containing all game entries.
        template_name (str): The template used to render the list of games.
        context_object_name (str): The context variable name for the list of games.
        paginate_by (int): The number of games to display per page.
    """
    queryset = Game.objects.all()  # Fetch all game entries
    template_name = "ssg_games/games.html"  # Specify the template to use
    context_object_name = "games"  # Name of the context variable
    paginate_by = 6  # Number of games per page

def game_detail(request, slug):
    """
    Display an individual :model:`ssg_games.Game`.

    **Context**

    ``game``
        An instance of :model:`ssg_games.Game`.
    
    **Template:**

    :template:`ssg_games/game_detail.html`
    """
    queryset = Game.objects.all()  # Fetch all game entries
    game = get_object_or_404(queryset, slug=slug)  # Fetch the game with the given slug

    return render(
        request,
        'ssg_games/game_detail.html',  # Render the game detail template
        {
            'game': game,  # Pass the game instance to the template
        }
    )