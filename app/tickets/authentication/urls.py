from django.conf.urls import url
from tickets.authentication.views import LoginView, RegistrationView, LogoutView


app_name = 'authentication'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
]
