from django.shortcuts import render
from .models import *
from datetime import date



def index(request):
    formats = date.today()
    games = Game.objects.all().order_by('home_team__league').filter(gamedates__dates=formats)
    premier = League.objects.all().order_by('league')
    gamedates = GameDates.objects.all().order_by('dates')
    
    context = {
        "games": games,
        "premier":premier,
        "gamedates":gamedates,
    }

    return render(request, 'index.html', context)

def gamesdates(request):
    formats = date.today()
    games = Game.objects.all().order_by('home_team__league').filter(gamedates__dates=formats)
    gamedates = GameDates.objects.all().order_by('dates')
    
    context = {
        "games": games,
        "gamedates":gamedates,
    }

    return render(request, 'gamesdates.html', context)

def detail(request, id, slug):
    details = Game.objects.get(pk = id)
    head = Headtohead.objects.get(pk=1)
   
    context = {
        "details":details,
        "head":head
    }
                    
    return render(request, 'detail.html', context)

























































































# def indexx(request):
#     premier = Game.objects.filter(premier="premier")
    
#     context = {
#         "premier": premier,
#     }
#     return render(request, "index.html", context)


# def indexx(request):
#     premier = Game.objects.filter(headhead__first_team__league='league')
    
#     context = {
#         "premier": premier,
#     }
#     return render(request, "index.html", context)

# def indexx(request):
#     premier = Product.objects.filter(category__title= title)
#     premier = Date.objects.filter(category__title= title)
    
#     context = {
#         "premier": premier,
#     }
#     return render(request, "index.html", context)