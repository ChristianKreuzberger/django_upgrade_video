from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView


from tickets.tickets.forms import CreateTicketForm
from tickets.tickets.models import Ticket


class ListTicketsView(View):
    template_name = 'tickets/list.html'

    def get(self, request):
        context = {
            'tickets': Ticket.objects.all()
        }

        return render(request, self.template_name, context)


# toDo: Try out CreateView
class CreateTicketView(View):
    """
    View for creating a new ticket
    """
    template_name = 'tickets/create.html'

    def get(self, request):
        create_ticket_form = CreateTicketForm()

        context = {
            'create_ticket_form': create_ticket_form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        create_ticket_form = CreateTicketForm(request.POST or None)

        context = {
            'create_ticket_form': create_ticket_form
        }

        current_user = request.user

        if create_ticket_form.is_valid():
            # ToDo: Replace with create_ticket_form.save()
            ticket = Ticket.objects.create(
                title=create_ticket_form.data['title'],
                description=create_ticket_form.data['description'],
                status=create_ticket_form.data['status'],
                created_by=current_user
            )

            # assignee is a M2M field which needs to be filled after we create the ticket
            ticket.assigned_to.add(create_ticket_form.data['assigned_to'])

            return HttpResponseRedirect(reverse('tickets:view', {'pk': ticket.pk}))

        return render(request, self.template_name, context)


class ViewTicketView(DetailView):
    template_name = 'tickets/view.html'

    model = Ticket


# toDo: Try out EditView
class EditTicketView(View):
    template_name = 'tickets/edit.html'

    def get(self, request, pk=None):
        ticket = get_object_or_404(Ticket.objects.all(), pk=pk)

        edit_ticket_form = CreateTicketForm(instance=ticket)

        context = {
            'ticket': ticket,
            'edit_ticket_form': edit_ticket_form
        }

        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        ticket = get_object_or_404(Ticket.objects.all(), pk=pk)

        edit_ticket_form = CreateTicketForm(request.POST or None, instance=ticket)

        context = {
            'ticket': ticket,
            'edit_ticket_form': edit_ticket_form
        }

        if edit_ticket_form.is_valid():
            edit_ticket_form.save()
            return HttpResponseRedirect(reverse('tickets:view', kwargs={'pk': ticket.pk}))

        return render(request, self.template_name, context)
