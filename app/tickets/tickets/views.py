from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View

from tickets.tickets.models import Ticket


class ListTicketsView(View):
    template_name = 'tickets/list.html'

    def get(self, request):
        context = RequestContext(request, {
            'tickets': Ticket.objects.all()
        })

        return render(request, self.template_name, context)


class CreateTicketView(View):
    template_name = 'tickets/create.html'

    def get(self, request):
        context = RequestContext(request, {
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class EditTicketView(View):
    template_name = ''

    def get(self, request):
        context = RequestContext(request, {
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass
