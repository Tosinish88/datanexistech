
from django.shortcuts import render
from pages.models import Service, Team




def allServices(request):
    allServices = Service.objects.all()
    return dict(allServices=allServices)


def team(request):
    team = Team.objects.all().order_by('-name')
    return dict(team=team)




