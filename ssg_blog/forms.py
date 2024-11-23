from django import forms
from .models import Comment

# Form for submitting comments on blog posts
class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on blog posts.

    Args:
        forms (_type_): _description_
    """
    class Meta:
        """
        Meta class for the CommentForm form.
        """
        model = Comment  # Specify the model to use for this form
        fields = ('body',)  # Specify the fields to include in the form