from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    name = 'Anonimo'

    if request.user.is_authenticated():

        name = request.user.username

    return render(request, 'body/index.html', {
                            'name' : name,
                            'user' : request.user
    })