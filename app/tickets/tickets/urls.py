from django.conf.urls import url

from tickets.tickets.views import ListTicketsView, CreateTicketView

urlpatterns = [
    url(r'^$', ListTicketsView.as_view(), name='list'),
    url(r'^create/$', CreateTicketView.as_view(), name='create'),
]
