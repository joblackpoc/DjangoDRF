from django.shortcuts import render

# Create your views here.
def home(request):
    templatefilename = 'commpany/home.html'
    return render(request, templatefilename)