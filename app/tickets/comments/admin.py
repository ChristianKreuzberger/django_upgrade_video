from django.contrib import admin

# Register your models here.
from tickets.comments.models import Comment

admin.site.register(Comment)
