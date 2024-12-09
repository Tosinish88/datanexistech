from django.shortcuts import render, redirect
from pages.models import Service
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def home(request):

    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        # Form submission logic
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')  # Redirect to prevent re-submission
        else:
            messages.error(request, 'There was an error with your submission. Please correct the fields.')
    else:
        # GET request: just render the contact page with an empty form
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

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


