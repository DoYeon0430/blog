from django import forms
from .models import Comment_physics,Comment_django,Comment_network

class Comment_physicsForm(forms.ModelForm):
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
        model = Comment_physics
        fields = ['username', 'password', 'content']

class Comment_djangoForm(forms.ModelForm):
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
        model = Comment_django
        fields = ['username', 'password', 'content']

class Comment_networkForm(forms.ModelForm):
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
        model = Comment_network
        fields = ['username', 'password', 'content']
