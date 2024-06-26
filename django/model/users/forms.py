from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# 유저 정보를 관리하는 UserCreationForm이 이미 있음
class UserForm(UserCreationForm):

    # 장고가 기본제공하는 유저모델 컬럼 중 일부 컬럼 not null 로 설정 가능
    email = forms.EmailField(label="이메일", help_text="사용할 이메일을 입력해 주세요")

    class Meta:
        model = User
        # password 자동으로 포함됨
        fields = ["username", "email"]
