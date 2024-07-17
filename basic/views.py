import datetime
import logging
from datetime import datetime, date
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
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

def ShowDateTime(request):
    TodayDate = datetime.datetime.now()
    templatefilename = "basic/Showtimeinfo.html"
    dict = {'TodayDate':TodayDate}
    return render(request, templatefilename, dict)

def LoggingExample(request):
    logging.debug(f"Debug : I just entered into the view..{datetime.now()}")
    logging.info(f"Info : Confirmation that things are working as expected.")
    logging.warning(f"Warning : An incident that something unexpected happened")
    logging.error(f"Error : Due to a more serious problem, the software has not been able to perform some function.")
    logging.critical(f"Critical : A serious error, indicating that the program itself may be unable to continue running.")

    custom_logger = logging.getLogger('mycustom_logger')
    custom_logger.debug(f"Debug : I just entered into the view..{datetime.now()}")
    custom_logger.info(f"Info : Confirmation that things are working as expected.")
    custom_logger.warning(f"Warning : An incident that something unexpected happened")
    custom_logger.error(f"Error : Due to a more serious problem, the software has not been able to perform some function.")
    custom_logger.critical(f"Critical : A serious error, indicating that the program itself may be unable to continue running.")
    
    return HttpResponse("Logging Demo")