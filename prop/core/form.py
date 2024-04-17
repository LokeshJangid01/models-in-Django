from django import forms
from .models import Rating,Restaurant

class RatingForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','date_opened','latitude','longitude','restaurant_type',)
