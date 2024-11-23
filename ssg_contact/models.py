"""
Models for the ssg_contact app.
"""
from django.db import models

# Create your models here.


class UserMessage(models.Model):
    """
    A model to store contact form submissions.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                             null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    message_read = models.BooleanField(default=False)
    message_replied = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} {self.email} - {self.subject}"
    