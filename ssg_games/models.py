from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


player_amount = (
    
    ('1', '1+'),
    ('2', '2+'),
    ('3', '3+'),
    ('4', '4+'),
    
)

game_length = (
    
    ('15-30', '15-30 minutes'),
    ('30-60', '30-60 minutes'),
    ('60+', '60+ minutes'),
    
)

class Game(models.Model):
    """
    Stores a section on each game
    """
    
    game_title = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    players = models.CharField(choices=player_amount, max_length=10)
    game_time = models.CharField(choices=game_length, max_length=50)
    game_image_main = CloudinaryField('image', default='placeholder')
    game_image_2 = CloudinaryField('image', default='placeholder', blank=True)
    game_image_3 = CloudinaryField('image', default='placeholder', blank=True)
    game_image_4 = CloudinaryField('image', default='placeholder', blank=True)
    game_image_5 = CloudinaryField('image', default='placeholder', blank=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.game_title} | Created by {self.creator}"