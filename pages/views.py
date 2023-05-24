from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/home.html')


def about(request): #pass a request to the method
    return render(request, 'pages/about.html') #pass again request and about.html path to render method to url folder

def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
