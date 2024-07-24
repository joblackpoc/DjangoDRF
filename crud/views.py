from django.shortcuts import render

# Create your views here.
def Home(request):
    templatefilename = 'crud/sharp-home.html'
    return render(request, templatefilename)