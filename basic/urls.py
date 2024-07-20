from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('index', views.Index, name='index'),
    path('home',views.Home ,name='home'),
    path('showmore',views.Showmoremessage, name='showmore'),
    path('usevariable', views.UseVariableAsResponse, name='usevariable'),
    path('getrequest', views.GetRequestVariable, name='getrequest'),
    path('showtime', views.ShowDateTime, name='showtime'),
    path('logging', views.LoggingExample, name='logging'),
    path('iftag', views.iftagdemo, name='iftag'),
    path('showproducts', views.ShowProducts, name='showproducts'),
    path('loadusers', views.LoadUsers, name='loadusers'),
    path('loadusers2', views.LoadUsers2, name='loadusers2'),
    path('showuserdetails', views.LoadUserDetails, name='showuserdetails'),
    path('passmodel', views.PassModelToTemplate, name='passmodel'),
    path('bif', views.BuiltInFiltersDemo, name='bif'),

]
