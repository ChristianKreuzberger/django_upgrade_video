from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View

from tickets.tickets.forms import CreateTicketForm
from tickets.tickets.models import Ticket


class ListTicketsView(View):
    template_name = 'tickets/list.html'

    def get(self, request):
        context = RequestContext(request, {
            'tickets': Ticket.objects.all()
        })

        return render(request, self.template_name, context)


class CreateTicketView(View):
    """
    View for creating a new ticket
    """
    template_name = 'tickets/create.html'

    def get(self, request):
        create_ticket_form = CreateTicketForm()

        context = RequestContext(request, {
            'create_ticket_form': create_ticket_form
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        create_ticket_form = CreateTicketForm(request.POST or None)

        context = RequestContext(request, {
            'create_ticket_form': create_ticket_form
        })

        current_user = request.user

        if create_ticket_form.is_valid():
            ticket = Ticket.objects.create(
                title=create_ticket_form.data['title'],
                description=create_ticket_form.data['description'],
                status=create_ticket_form.data['status'],
                created_by=current_user
            )

            # assignee is a M2M field which needs to be filled after we create the ticket
            ticket.assigned_to.add(create_ticket_form.data['assigned_to'])

            # ToDo: redirect to ticket detail view once ready
            return HttpResponseRedirect(reverse('tickets:list'))

        return render(request, self.template_name, context)


class EditTicketView(View):
    template_name = ''

    def get(self, request):
        context = RequestContext(request, {
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass
