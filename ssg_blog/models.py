
"""
This module contains the models for the blog application.

Models:
    Post: Stores a single blog post entry, related to :model:`auth.User`.
    Comment: Stores a single comment entry, related to :model:`blog.Post` and :model:`auth.User`.
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS =((0, "Draft"), (1, "Published"))


# Post Model
class Post(models.Model):
    """
    Stores a single blog post entry, related to :model:`auth.User`.

    Attributes:
        title (CharField): The title of the blog post, unique.
        slug (SlugField): The slug for the blog post, unique.
        author (ForeignKey): The author of the blog post, related to :model:`auth.User`.
        featured_image (CloudinaryField): The featured image for the blog post.
        content (TextField): The main content of the blog post.
        created_on (DateTimeField): The date and time when the blog post was created.
        status (IntegerField): The status of the blog post, either Draft or Published.
        excerpt (TextField): A short excerpt of the blog post.
        updated_on (DateTimeField): The date and time when the blog post was last updated.
        is_featured (BooleanField): Indicates if the blog post is featured.

    Meta:
        ordering: Orders the blog posts by creation date in descending order.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    # Meta class and assigning string names to Post objects
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# Comment Model
class Comment(models.Model):
    """
    Stores a single comment entry, related to :model:`blog.Post` and :model:`auth.User`.

    Attributes:
        post (ForeignKey): The blog post that the comment is related to, related to :model:`blog.Post`.
        author (ForeignKey): The author of the comment, related to :model:`auth.User`.
        body (TextField): The main content of the comment.
        approved (BooleanField): Indicates if the comment is approved.
        created_on (DateTimeField): The date and time when the comment was created.

    Meta:
        ordering: Orders the comments by creation date in descending order.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # Meta class and assigning string names to Post objects
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body} by {self.author}"