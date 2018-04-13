from django import forms

from tickets.comments.models import Comment


class CreateCommentForm(forms.ModelForm):
    """
    Provides a form for creating a new comment on a ticket
    """

    class Meta:
        model = Comment
        fields = ('text', )
