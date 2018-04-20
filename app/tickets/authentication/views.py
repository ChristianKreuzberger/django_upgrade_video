from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View

from tickets.authentication.forms import LoginForm, RegistrationForm

User = get_user_model()


class LoginView(View):
    """
    A basic login view
    """
    template_name = 'authentication/login.html'

    def get(self, request):
        form = LoginForm()

        context = RequestContext(request, {
            'form': form
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        context = RequestContext(request, {
            'form': form
        })

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    context.update({'inactive': True})
            else:
                # the authentication system was unable to verify the username and password
                context.update({'wrong_credentials': True})

        return render(request, self.template_name, context)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class RegistrationView(View):
    """
    A basic registration view
    """
    template_name = 'authentication/registration.html'

    def get(self, request):
        form = RegistrationForm()

        context = RequestContext(request, {
            'form': form
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            # sign up a new user
            User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])

            # Todo: Show the user a notification

            # ToDo: redirect to login view
            return HttpResponseRedirect('/')

        context = RequestContext(request, {
            'form': form
        })

        return render(request, self.template_name, context)
