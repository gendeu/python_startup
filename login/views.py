from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # return HttpResponse(request, 'Hello World')
    # return render(request, 'login.html')
    return render(request, 'login.html', {'name':'Deo'})