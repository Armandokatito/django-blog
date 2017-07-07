from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from userprofile.forms import UserProfileForm


# Create your views here.
@login_required
def user_profile(request):
    args = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')
        else:

            args.update(csrf(request))
            args['form'] = form

    return render(request, 'body/profile.html', args)