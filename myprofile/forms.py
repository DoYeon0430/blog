from django import forms
from .models import MeetingDate
from .models import Post, PostImage, PostChat

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
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': '제목을 입력하세요.'}),
            'username': forms.TextInput(attrs={'placeholder': '이름을 입력하세요.'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 작성하세요.'}),
        }


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

PostImageFormSet = forms.inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1, max_num=5)

class PostChatForm(forms.ModelForm):
    class Meta:
        model = PostChat
        fields = ['username', 'message']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '이름을 입력하세요.'}),
            'message': forms.Textarea(attrs={'placeholder': '내용을 작성하세요.'}),
        }