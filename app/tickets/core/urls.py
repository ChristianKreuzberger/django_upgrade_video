from django.conf.urls import url
from tickets.core.views import MainView

app_name = 'core'

urlpatterns = [
    url(r'^$', MainView.as_view(), name='home'),
]
