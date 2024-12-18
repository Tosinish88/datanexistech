# forms.py
from django import forms
from .models import ContactMessage, Subscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['firstname', 'lastname', 'email', 'message']



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control course-text-bg',
                'placeholder': 'Enter your email',
                'required': 'required',
            }),
        }
        labels = {
            'email': '',
        }

    # Custom email validation (if needed)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please enter your email.")
        return email