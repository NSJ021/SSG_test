from django.urls import path
from . import views

urlpatterns = [
    path('', views.games, name="games"),
    # path('<slug:slug>/', views.game_detail, name='game_details'),
]
