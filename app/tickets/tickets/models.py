from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


TICKET_STATUS_NEW = 'new'
TICKET_STATUS_PROGRESS = 'pro'
TICKET_STATUS_FINISHED = 'fin'
TICKET_STATUS_TESTING = 'tes'
TICKET_STATUS_WONTFIX = 'wfx'

TICKET_STATUS_CHOICES = (
    (TICKET_STATUS_NEW, _('New')),
    (TICKET_STATUS_PROGRESS, _('In progress')),
    (TICKET_STATUS_FINISHED, _('Finished')),
    (TICKET_STATUS_TESTING, _('Testing')),
    (TICKET_STATUS_WONTFIX, _('Wont fix'))
)


class Ticket(models.Model):
    """
    A ticket with a title, description, and a status
    Has a many to many relation ship to users
    """

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")

    title = models.CharField(
        max_length=128,
        verbose_name=_("Title of the ticket")
    )

    description = models.TextField(
        verbose_name=_("Description of the ticket")
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tickets_created_by_user",
        verbose_name=_("Who created the ticket")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("When was the ticket created")
    )

    status = models.CharField(
        max_length=3,
        choices=TICKET_STATUS_CHOICES,
        default=TICKET_STATUS_NEW,
        verbose_name=_("What is the status of the ticket")
    )

    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Who is responsible for the ticket")
    )

    def __str__(self):
        return "Ticket {id}: {title}".format(
            id=self.id, title=self.title
        )

