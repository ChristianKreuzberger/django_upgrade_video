from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from tickets.tickets.models import Ticket, TICKET_STATUS_FINISHED

User = get_user_model()


class MainView(View):
    template_name = 'main/main.html',

    def get(self, request):
        current_user = request.user

        context = {
            'is_authenticated': current_user.is_authenticated,
            'user': current_user
        }

        if current_user.is_authenticated:
            # fetch all tickets of that user
            tickets = Ticket.objects.filter(assigned_to=current_user).exclude(status__in=[
                TICKET_STATUS_FINISHED
            ])
            context.update({'your_tickets': tickets})

        return render(request, self.template_name, context)
