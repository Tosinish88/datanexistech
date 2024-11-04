from django.shortcuts import render
from pages.models import Service

# Create your views here.


def home(request):

    return render(request, 'home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def projects(request):
    return render(request, 'pages/projects.html')

def about(request):
    return render(request, 'pages/about.html')

def single_service(request, slug):
    service = Service.objects.get(service__slug=slug)
    allServe = Service.objects.exclude(id=service.id)

    # print('allServe ======', allServe)
    print('service ======', service.service.title)

    context = {
        'service': service,
        'allServe': allServe,
    }
    return render(request, 'pages/single_service.html', context)


