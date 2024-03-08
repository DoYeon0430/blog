from django import forms
from .models import MeetingDate

class MeetingDateForm(forms.ModelForm):
    class Meta:
        model = MeetingDate
        fields = ['date', 'text', 'details', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': '날짜를 입력하세요'}),
            'text': forms.TextInput(attrs={'placeholder': 'ex) 서울시 은평구'}),
            'details': forms.TextInput(attrs={'placeholder': 'ex) 연신내 달빛포차'}),
            'description': forms.Textarea(attrs={'placeholder': '이미지 설명을 입력하세요'}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = MeetingDate
        fields = ['photo', 'description']