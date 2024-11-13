from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Team(models.Model):
    """
    Stores a section about the team
    """
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.position