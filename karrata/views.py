from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from samplesite.forms import MyRegistrationForm


# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

def logout(request):

    auth.logout(request)

    return HttpResponseRedirect('/')

def loggedin(request):
    return HttpResponse("loggedin")
def invalid_login(request):
    return HttpResponse("Invalid loggedin")

######## REGISTER #################
def register(request):

    return render(request, 'auth/register.html')

def register_auth(request):

    if request.method == 'POST':

        form = MyRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/success')
    args = {}
    args['form'] = MyRegistrationForm()

    return render(request, 'auth/register.html', args)

def register_success(request):
    return HttpResponse("Conta criada com sucesso! faca <a href='/'>login</a>")
