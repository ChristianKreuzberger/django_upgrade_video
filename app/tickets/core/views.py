from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.template import Context

User = get_user_model()


class MainView(View):
    template_name = 'main/main.html',

    def get(self, request):
        context = Context({
            'is_authenticated': request.user.is_authenticated()
        })

        return render(request, self.template_name, context)
