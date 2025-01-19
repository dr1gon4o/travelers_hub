from django import forms
from .models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country', 'about_me']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Enter a unique nickname...'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter a valid email address...'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter a country code like <BGR>...'
            }),
            'about_me': forms.Textarea(attrs={
                'placeholder': 'Tell us something about yourself...',
                'rows': 3,
            }),
        }
