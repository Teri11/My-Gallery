from django.http  import HttpResponse,Http404
from django.shortcuts import render
from .models import Category,Picture


# Create your views here.
def home(request):
    picture=Picture.objects.all()   
    return render(request, 'index.html',{'picture':picture[::-1],})