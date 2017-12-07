from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.views.generic import View

from tickets.authentication.forms import LoginForm, RegistrationForm

User = get_user_model()


class LoginView(View):
    """
    A basic login view
    """
    template_name = 'authentication/login.html',

    def get(self, request):
        form = LoginView()

        context = Context({
            'form': form
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # ToDo: log the user in using auth backend

            # ToDo: redirect to login view
            return HttpResponseRedirect('/success/')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class RegistrationView(View):
    """
    A basic registration view
    """
    template_name = 'authentication/registration.html'

    def get(self, request):
        form = RegistrationForm()

        context = Context({
            'form': form
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm()
        if form.is_valid():
            # sign up a new user
            User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])

            # ToDo: redirect to login view
            return HttpResponseRedirect('/success/')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)