from django import forms
from order.models import Booknow

class booknowform(forms.ModelForm):
    class Meta:
        model=Booknow
        fields=['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }