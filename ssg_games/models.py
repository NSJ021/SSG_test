"""
This module contains the models for the game application.

Models:
    Game: Stores a single game entry.
"""

from django.db import models
from cloudinary.models import CloudinaryField

# Player Amount and Game Length Choices
player_amount = (
    ('1+', '1+'),
    ('2+', '2+'),
    ('3+', '3+'),
    ('4+', '4+'),  
)

game_length = (
    ('15-30', '15-30 minutes'),
    ('30-60', '30-60 minutes'),
    ('60+', '60+ minutes'),
)

# Game Model
class Game(models.Model):
    """
    Stores a section on each game.

    Attributes:
        game_title (CharField): The title of the game.
        slug (SlugField): The slug for the game, unique.
        creator (CharField): The creator of the game.
        players (CharField): The number of players required for the game.
        game_time (CharField): The length of time to play the game.
        game_image_main (CloudinaryField): The main image for the game.
        game_image_2 (CloudinaryField): An optional second image for the game.
        game_image_3 (CloudinaryField): An optional third image for the game.
        game_image_4 (CloudinaryField): An optional fourth image for the game.
        game_image_5 (CloudinaryField): An optional fifth image for the game.
        game_brief (TextField): A brief description of the game.
        description (TextField): A detailed description of the game.
        is_featured (BooleanField): Indicates if the game is featured.
    """
    
    game_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.CharField(max_length=200)
    players = models.CharField(choices=player_amount, max_length=10)
    game_time = models.CharField(choices=game_length, max_length=50)
    game_image_main = CloudinaryField('image', default='placeholder')
    game_image_2 = CloudinaryField('image', blank=True)
    game_image_3 = CloudinaryField('image', blank=True)
    game_image_4 = CloudinaryField('image', blank=True)
    game_image_5 = CloudinaryField('image', blank=True)
    game_brief = models.TextField()
    description = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game_title} | Created by {self.creator}"