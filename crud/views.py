from django.shortcuts import render

# Create your views here.
def Home(request):
    templatefilename = 'crud/index.html'
    return render(request, templatefilename)