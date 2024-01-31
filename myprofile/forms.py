from django import forms
from .models import MeetingDate

class MeetingDateForm(forms.ModelForm):
    class Meta:
        model = MeetingDate
        fields = ['date', 'text', 'details']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }