from django import forms
from .models import AliceUser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    userName = forms.CharField(error_messages={'required': '아이디를 입력해주세요.'}, max_length=64, label="사용자 이름")
    passWord = forms.CharField(error_messages={'required': '비밀번호를 입력해주세요.'}, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        userName = cleaned_data.get('userName')
        passWord = cleaned_data.get('passWord')

        if userName and passWord:
            aliceUser = AliceUser.objects.get(userName=userName)
            if not check_password(passWord, aliceUser.passWord):
                self.add_error('passWord', '비밀번호가 틀렸습니다.')
            else:
                self.user_id = aliceUser.id