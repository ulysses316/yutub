from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import UserForm
import crypt
# Create your views here.

def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            form.save()
            return redirect("hola")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'content/form_user.html', {'form': form})


def hola_mundo(request):
    return HttpResponse("Thanks")