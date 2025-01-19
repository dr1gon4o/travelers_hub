from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']
        widgets = {
            'destination': forms.TextInput(attrs={
                'placeholder': 'Enter a destination...'
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': 'Briefly describe your trip...',
                'rows': 4
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
            'duration': forms.NumberInput(attrs={
                'min': 1,
                'placeholder': 'Enter duration in days...'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Optional: Provide a URL to an image...'
            }),
        }
