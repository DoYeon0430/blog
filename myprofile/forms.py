from django import forms
from .models import MeetingDate

class MeetingDateForm(forms.ModelForm):
    class Meta:
        model = MeetingDate
        fields = ['date', 'text', 'details', 'photo', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.TextInput(attrs={'placeholder': 'ex) 서울시 은평구'}),
            'details': forms.TextInput(attrs={'placeholder': 'ex) 연신내 달빛포차'}),
            'photo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'placeholder': '느낀점을 입력하세요.'}),
        }