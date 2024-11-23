"""
Views for the ssg_accounts app.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from ssg_blog.models import Comment as BlogComment
from ssg_games.models import Comment as GameComment
from ssg_contact.models import UserMessage

# Create your views here.

# Signup view
def signup(request):
    """
    View for signing up the user.
    """
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # Check if passwords match
        if password == confirm_password:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            else:
                # Check if email already exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('signup')
                else:
                    # Create user
                    user = User.objects.create_user(
                        username=username, password=password, email=email,
                        first_name=firstname, last_name=lastname)
                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'ssg_accounts/signup.html')

# Login view
def login(request):
    """
    View for logging in the user.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # Check if user exists
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'ssg_accounts/login.html')

# Logout view
def logout(request):
    """
    View for logging out the user.
    """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    """
    View for the user dashboard.
    """
    # Get both types of comments
    blog_comments = BlogComment.objects.filter(author=request.user).select_related('post')
    game_comments = GameComment.objects.filter(author=request.user).select_related('game')
    user_messages = UserMessage.objects.filter(user_id=request.user)
    
    context = {
        'blog_comments': blog_comments,
        'game_comments': game_comments,
        'user_messages': user_messages,
        'is_superuser': request.user.is_superuser,
    }
    return render(request, 'ssg_accounts/dashboard.html', context)
