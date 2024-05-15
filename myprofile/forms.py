from django import forms
from .models import MeetingDate
from .models import Post, PostImage

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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'username', 'content']


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

PostImageFormSet = forms.inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1, max_num=5)