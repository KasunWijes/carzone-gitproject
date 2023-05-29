from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()  #models.object all vlaues
    data = {
     'teams' :teams,
    }
    return render(request,'pages/home.html', data)  #pass the data into home page


def about(request): #pass a request to the method
    teams = Team.objects.all()
    data = {
        'teams' :teams,
    }
    return render(request, 'pages/about.html', data) #pass again request and about.html path to render method to url folder

def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
