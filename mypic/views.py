
from email.mime import image
from django.shortcuts import render
from .models import Category,Picture


# Create your views here.
def home(request):
    picture=Picture.objects.all()   
    return render(request, 'index.html',{'picture':picture[::-1],})



def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_articles = Picture.search_by_category( category)
        message = f"{ category}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
    