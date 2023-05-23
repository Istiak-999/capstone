from django.shortcuts import render
from .models import PostModel
#from django.http import HttpResponse
#from . import urls
# Create your views here.
def index(request):
    posts=PostModel.objects.all()
    
    return render(request,'blog/index.html',{'posts':posts})

