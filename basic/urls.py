from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home ,name='home'),
    path('showmore',views.Showmoremessage, name='showmore'),
    path('usevar', views.UseVariableAsResponse, name='usevar'),
    path('getrequest', views.GetRequestVariable, name='getrequest'),
    path('showtime', views.ShowDateTime, name='showtime'),
]
