from django.shortcuts import render
from ssg_games.models import Game

# Create your views here.

def games(request):
    game = Game.objects.order_by('game_title')
    
    return render(request, 'ssg_games/games.html',
                  {
            'games': game
        },
    )