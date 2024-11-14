from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from ssg_games.models import Game

# Create your views here.



class Games(generic.ListView):
    """
    Renders a list of all the games with the database
    """
    queryset = Game.objects.all()
    template_name = "ssg_games/games.html"
    context_object_name = "games"
    paginate_by = 6


def game_detail(request, slug):
    """
    Display an individual :model:`ssg_games.Game`.

    **Context**

    ``game``
        An instance of :model:`ssg_games.Game`.
    
    **Template:**

    :template:`game_details.html`
    """

    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        'ssg_games/game_detail.html',
        {
            'game': game,
        }
    )