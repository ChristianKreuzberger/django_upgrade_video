from django.conf.urls import url
from tickets.core.views import MainView

urlpatterns = [
    url(r'', MainView.as_view()),
]
