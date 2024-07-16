from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h1>Hello world from Django 5!</h1>")

def Showmoremessage(request):
    return HttpResponse("<h1>Hello world from Django 5!</h1><h2>Hello world from Django 5!</h2><h3>Hello world from Django 5!</h3>")

def UseVariableAsResponse(request):
    Message = "<h1>Hello world from Django 5!</h1>"
    Message += "<h2>Hello world from Django 5!</h2>"
    Message += "<h3>Hello world from Django 5!</h3>"
    Message += "<h4>Hello world from Django 5!</h4>"
    Message += "<h5>Hello world from Django 5!</h5>"
    return HttpResponse(Message)

def GetRequestVariable(request):
    Message = ''
    if(request.method == 'GET'):
        if(request.GET.get('Message')):
            Message = request.GET.get('Message')
        else:
            Message = "You haven't supplied a message paremeter yet."
    return HttpResponse(Message)