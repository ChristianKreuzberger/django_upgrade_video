from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import View

from tickets.comments.forms import CreateCommentForm
from tickets.tickets.models import Ticket


class CreateCommentView(View):
    """
    View for creating a new comment on a ticket
    """

    template_name = 'comments/create.html'

    def get(self, request, pk, *args, **kwargs):
        ticket = get_object_or_404(Ticket.objects.all(), pk=pk)

        create_comment_form = CreateCommentForm()

        context = {
            'ticket': ticket,
            'create_comment_form': create_comment_form
        }

        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        ticket = get_object_or_404(Ticket.objects.all(), pk=pk)

        create_comment_form = CreateCommentForm(
            request.POST or None
        )

        context = {
            'ticket': ticket,
            'create_comment_form': create_comment_form
        }

        current_user = request.user

        if create_comment_form.is_valid():
            comment = create_comment_form.save(commit=False)
            comment.ticket = ticket
            comment.created_by = current_user
            comment.save()

            # on success, redirect to the ticket detail view
            return HttpResponseRedirect(reverse('tickets:view', kwargs={'pk': pk}))

        return render(request, self.template_name, context)
