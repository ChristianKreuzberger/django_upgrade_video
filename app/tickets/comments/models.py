from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Comment(models.Model):
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('created_at',)

    text = models.TextField(
        verbose_name=_("Comment")
    )

    ticket = models.ForeignKey(
        'tickets.Ticket',
        verbose_name=_("Which ticket is this comment for"),
        on_delete=models.CASCADE,
        related_name='comments',
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments_created_by_user",
        verbose_name=_("Who created the comment"),
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("When was the comment created"),
        db_index=True
    )

    def __str__(self):
        return _("Comment from %(date)s on ticket %(ticket)s") % {'date': self.created_at, 'ticket': self.ticket}
