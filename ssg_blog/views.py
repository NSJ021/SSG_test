"""
This module contains the views for the blog application.

Views:
    Blog: Renders a list of all the blog posts in the database.
    post_detail: Displays an individual blog post entry along with its comments.
    comment_edit: Displays an individual comment for editing.
"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.

class Blog(generic.ListView):
    """
    Renders a list of all the blog posts in the database.

    Attributes:
        queryset (QuerySet): The queryset containing all published blog posts.
        template_name (str): The template used to render the list of blog posts.
        paginate_by (int): The number of blog posts to display per page.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "ssg_blog/blog.html"
    paginate_by = 6

# Post details view
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    
    return render(
        request,
        "ssg_blog/post_detail.html",
        {
            "post": post,
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

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
       single comment related to the post

    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))  