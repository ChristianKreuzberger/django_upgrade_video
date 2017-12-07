from django.conf.urls import url
from tickets.authentication.views import LoginView, RegistrationView


urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^registration/', RegistrationView.as_view(), name='registration'),
]
