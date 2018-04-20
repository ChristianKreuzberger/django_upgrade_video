from django.conf.urls import url

from tickets.tickets.views import ListTicketsView, CreateTicketView, ViewTicketView, EditTicketView

app_name = 'tickets'

urlpatterns = [
    url(r'^$', ListTicketsView.as_view(), name='list'),
    url(r'^create/$', CreateTicketView.as_view(), name='create'),
    url(r'^view/(?P<pk>[0-9]+)/$', ViewTicketView.as_view(), name='view'),
    url(r'^edit/(?P<pk>[0-9]+)/$', EditTicketView.as_view(), name='edit'),
]
