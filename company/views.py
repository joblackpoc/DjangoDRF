from django.shortcuts import render

# Create your views here.
def Home(request):
    templatefilename = 'company/home.html'
    return render(request, templatefilename)