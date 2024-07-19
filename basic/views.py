import datetime
import logging
import requests
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
    TodayDate = datetime.now()
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

def iftagdemo(request):
    data = {'name':'Jimmy Anderson', 'isVisible':True, 'login':False,'CountryCode':'IN', 'workExperience':15 }
    templatefilename = 'basic/Iftagdemo.html'
    dict = {"Data":data}
    return render(request, templatefilename, dict)

def ShowProducts(request):
    Processors = [{'Category':'AMD', 'processors':['Ryzen 3990', 'Ryzen 3970', 'Ryzen 3950']},
                  {'Category':'Intel', 'processors':['Xeon 8362', 'Xeon 8358', 'Xeon 8380']}
                  ]
    Products=[]
    Products.append({'productID':1, 'productName':'AMD Ryzen 3990', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':3000})
    Products.append({'productID':2, 'productName':'AMD Ryzen 3980', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':4000})
    Products.append({'productID':3, 'productName':'AMD Ryzen 3970', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':5000})
    Products.append({'productID':4, 'productName':'AMD Ryzen 3960', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':6000})
    Products.append({'productID':5, 'productName':'AMD Ryzen 3950', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':7000})
    Products.append({'productID':6, 'productName':'AMD Ryzen 3940', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':8000})
    Products.append({'productID':7, 'productName':'AMD Ryzen 3930', 'quantity':100, 'unitInStock':50, 'disContinued':False, 'cost':9000})
    Products.append({'productID':8, 'productName':'AMD Ryzen 3920', 'quantity':100, 'unitInStock':50, 'disContinued':True, 'cost':10000})
    Products.append({'productID':9, 'productName':'AMD Ryzen 3910', 'quantity':100, 'unitInStock':50, 'disContinued':True, 'cost':11000})
    Products.append({'productID':10, 'productName':'AMD Ryzen 3900', 'quantity':100, 'unitInStock':50, 'disContinued':True, 'cost':12000})
    TemplateFile = 'basic/Showproducts.html'
    dict = {'Products':Products, 'TotalProducts':len(Products), 'Processors':Processors }
    return render(request, TemplateFile, dict)

def LoadUsers(request):
    templatefilename = 'basic/Showusers.html'
    response = CallRestAPI()
    dict = {'users':response.json()}
    return render(request, templatefilename, dict)
def CallRestAPI():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users')
    return(response)

def LoadUsers2(request):
    templatefilename = 'basic/ShowusersAsCard.html'
    image = 'https://i.pravatar.cc'
    response = CallRestAPI()
    dict = {'users':response.json(), 'image':image}
    return render(request, templatefilename, dict)

def Index(request):
    return render(request, 'basic/Index.html')

def CallRestAPI2(userid):
    BASE_URL = 'https://fakestoreapi.com'
    reponse = requests.get(f'{BASE_URL}/users/{userid}')
    return(reponse)

def LoadUserDetails(request):
    templatefilename = 'basic/Showuserdetails.html'
    counter = 1
    response = CallRestAPI2(counter)
    image = 'https://i.pravatar.cc'
    dict = {'user':response.json(), 'image':image}
    return render(request, templatefilename, dict)
