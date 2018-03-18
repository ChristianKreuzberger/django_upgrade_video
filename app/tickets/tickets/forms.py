from django import forms

from tickets.tickets.models import Ticket


class CreateTicketForm(forms.ModelForm):
    """
    Provides a form for creating a new ticket
    """

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'status', 'assigned_to', )
