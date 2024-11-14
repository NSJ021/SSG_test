from django.urls import path
from . import views

urlpatterns = [
    path('', views.Games.as_view(), name="games"),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
]
