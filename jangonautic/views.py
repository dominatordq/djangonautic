from django.http import HttpResponse # allows a response to be sent to user
from django.shortcuts import render # allows for rendering html templates in the browser

def home(request):
    # return HttpResponse('homepage') # return http string
    return render(request, 'home.html') # Django knows where template folder is

def about(request):
    # return HttpResponse('about')    
    return render(request, 'about.html')
