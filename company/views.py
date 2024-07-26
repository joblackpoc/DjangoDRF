from django.shortcuts import render
from . models import Post
# Create your views here.
def Home(request):
    welcome = Post.objects.all()
    templatefilename = 'company/home.html'
    context = {
        'welcome':welcome
    }
    return render(request, templatefilename, context)