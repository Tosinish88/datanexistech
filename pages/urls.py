from django.urls import path, include

from .views import(
    home,
    contact,
    projects,
    about,
    single_service,
    subscribe,
)


urlpatterns = [
    path('', home, name='home'), 
    path('home/', home, name='home'), 
    path('contact/', contact, name='contact'), 
    path('projects/', projects, name='projects'), 
    path('about/', about, name='about'), 
    path('single_service/<str:slug>/', single_service, name='single_service'), 
    path('subscribe/', subscribe, name='subscribe'),
    # path('projects/', projects, name='projects'), 
    # path('projects/', projects, name='projects'), 
]

