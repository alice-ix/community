from django import forms

class LoginForm(forms.Form):
    userName = forms.CharField(max_length=64, label="사용자 이름")
    passWord = forms.CharField(widget=forms.PasswordInput, label="비밀번호")