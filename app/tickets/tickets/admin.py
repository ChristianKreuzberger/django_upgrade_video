from django.contrib import admin
from django.contrib.auth import get_user_model

from tickets.tickets.models import Ticket

User = get_user_model()

admin.site.register(Ticket)
