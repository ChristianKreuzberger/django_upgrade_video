from django.conf.urls import url

from tickets.comments.views import CreateCommentView

app_name = 'comments'

urlpatterns = [
    url(r'^view/(?P<pk>[0-9]+)/create_comment$', CreateCommentView.as_view(), name='create'),
]
