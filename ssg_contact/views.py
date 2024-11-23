"""
Views for the ssg_contact app.
"""
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserMessage

# Create your views here.

def user_contact(request):
    """
    Renders the contact page.

    **Template:**

    :template:`ssg_contact/contact.html`
    """
    if request.method == 'POST':
        # Get the form data
        user = request.user if request.user.is_authenticated else None
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone']
        message = request.POST['message']
        # Check if the user has already sent a message
        if request.user.is_authenticated:   
            user = request.user
            has_contacted = UserMessage.objects.filter(user_id=user, email=email)
            if has_contacted.exists():
            # Check if any of the messages have not been replied to
                if has_contacted.filter(message_replied=False).exists():
                    messages.error(
                        request, 'You have already sent a message, Please wait for a response')
                    return redirect('contact')
        # Save new User message
        new_contact = UserMessage(user_id=user.id if user else None, name=name, email=email,
                              subject=subject, phone_number=phone_number,
                              message=message)
        new_contact.save()
        messages.success(request, 'Your message has been sent successfully')
        # Send an email
        # send_mail(
        #     'Contact Form Submission',
        #     f'Name: {name}\nEmail: {email}\nMessage: {message}',
        #     email,
        #     [settings.DEFAULT_FROM_EMAIL],
        #     fail_silently=False,
        # )

        # Render the contact page template
        return redirect('contact')
    else:
        # Render the contact page template
        return render(request, 'ssg_contact/contact.html')
    