# -*- coding: utf-8 -*-
from threading import local

_thread_locals = local()


def set_current_request(request):
    """
    Binds the request to the current thread.
    :param request: Django request object
    :return:
    """
    return setattr(_thread_locals, '__request_middleware__current_request', request)


def get_current_request():
    """
    Gets the request from the current thread.
    :return: Django request object
    """
    return getattr(_thread_locals, '__request_middleware__current_request', None)


class StoreRequestMiddleware(object):
    """Middleware StoreRequestMiddleware

    This middleware saves the currently processed request
    in the working thread. This allows us to access the
    request everywhere, and don't need to pass it to every
    function.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        set_current_request(request)

        response = self.get_response(request)

        set_current_request(None)

        # Code to be executed for each request/response after
        # the view is called.

        return response
