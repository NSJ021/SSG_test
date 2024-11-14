"""
This module contains the models for the team application.

Models:
    Team: Stores a single team member entry.
"""

from django.db import models
from cloudinary.models import CloudinaryField

# Team Model
class Team(models.Model):
    """
    Stores a section about the team.

    Attributes:
        first_name (CharField): The first name of the team member.
        last_name (CharField): The last name of the team member.
        position (CharField): The position of the team member.
        profile_image (CloudinaryField): The profile image of the team member.
        content (TextField): Additional content about the team member.
        updated_on (DateTimeField): The date and time when the team member's information was last updated.
    """
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.position