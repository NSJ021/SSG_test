"""
This module contains the views for the game application.

Views:
    Games: Renders a list of all the games in the database.
    game_detail: Displays an individual game entry.
"""

from django.shortcuts import render, get_object_or_404, reverse  # Import render and get_object_or_404 for rendering templates and fetching objects
from django.views import generic  # Import generic views for class-based views
from ssg_games.models import Game, Comment  # Import the Game model
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.core.paginator import Paginator  # Import Paginator for paginating the list of games

# Create your views here.

def games(request):
    """
    Renders a list of all the games in the database.

    Attributes:
        queryset (QuerySet): The queryset containing all game entries.
        template_name (str): The template used to render the list of games.
        context_object_name (str): The context variable name for the list of games.
        paginate_by (int): The number of games to display per page.
    """
    games = Game.objects.order_by('game_title')  # Fetch all game entries ordering by game_title (alphabetically)
    paginator = Paginator(games, 4)  # Paginate the queryset by 4 games per page
    page = request.GET.get('page')  # Get the current page number
    paged_games = paginator.get_page(page)  # Get the games for the current page

    context = {
        'games': paged_games  # Pass the paginated games to the template
    }

    return render(request, 'ssg_games/games.html', context)


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
    comments = game.game_comments.all().order_by("-created_on")
    comment_count = game.game_comments.filter(approved=True).count()

    if request.method == "POST":
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.game = game
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    
    return render(
        request,
        "ssg_games/game_detail.html",
        {
            "game": game,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },

    )

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for editing.

    **Context**

    ``comment``
        An instance of :model:`blog.Comment`.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`comment_edit.html`
    """
    if request.method == "POST":

        queryset = Game.objects.all()
        game = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.game = game
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('game_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
       single comment related to the post

    """
    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('game_detail', args=[slug]))  