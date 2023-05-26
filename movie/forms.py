from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    username = forms.CharField(
        max_length=32,
        label="사용자 이름",
        error_messages={'required': '아이디를 입력해 주세요'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호",
        error_messages={'required': '비밀번호를 입력해 주세요'}
    )

    class Meta:
        model = Comment
        fields = ['username', 'password', 'content']
