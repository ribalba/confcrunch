from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'email', 'feedback']
        widgets = {
            'rating': forms.HiddenInput(),
        }
