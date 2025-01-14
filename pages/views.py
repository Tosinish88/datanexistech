from django.http import JsonResponse
from django.shortcuts import render, redirect
from pages.models import Service
from django.contrib import messages
from .forms import ContactForm, SubscriptionForm

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


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            try:
                # Save the subscription
                form.save()
                messages.success(request, 'You have subscribed successfully!')
                # Redirect to the same page to clear the form
                return redirect(f'{request.path}#services') # return to the exact part of the page
            except Exception:
                messages.error(request, 'This email is already subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
            return redirect(f'{request.path}#services')
    else:
        form = SubscriptionForm()

    # Render a fresh form if it's a GET request or after redirect
    return render(request, 'pages/about.html', {'form': form})



def custom_error_view(request, exception=None, error_code=500, error_message="Internal Server Error"):
    context = {
        "error_code": error_code,
        "error_message": error_message,
    }
    return render(request, 'pages/error.html', context, status=error_code)

def custom_400_view(request, exception=None):
    return custom_error_view(request, exception, error_code=400, error_message="Bad Request")

def custom_404_view(request, exception=None):
    return custom_error_view(request, exception, error_code=404, error_message="Page Not Found")

def custom_500_view(request):
    return custom_error_view(request, error_code=500, error_message="Internal Server Error")


