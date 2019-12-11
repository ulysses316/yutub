from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import UserForm
# Create your views here.

def formUser(request):
    if request.method == 'POST':
        form = UserForm(requests.POST)
       # if form.is_valid():
        #    form.save()
        return redirect("/hola")
    else:
        form = UserForm()
    return render(request,'content/form_user.html', {"form":form})

def hola_mundo(request):
    return render(request, 'content/video.html')