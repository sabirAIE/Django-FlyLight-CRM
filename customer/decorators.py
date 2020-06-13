from django.http import HttpResponse
from django.shortcuts import redirect

#decorators
def userAuthRequired(viewFunction):
    def wraperFunction(request, *args, **kwargs):
        try:
            user = request.session['user_id']
            if user is not None:
                return viewFunction(request, *args, **kwargs)
        except KeyError:
            return redirect('login')
    return wraperFunction


def userAuthReady(viewFunction):
    def wraperFunction(request, *args, **kwargs):
        try:
            user = request.session['user_id']
            if user is not None:
                return redirect('welcome')
        except KeyError:
                return viewFunction(request, *args, **kwargs)
    return wraperFunction