from django import forms
from .models import Photo


# ModelForm : 모델과 연결된 폼
# (Photo 모델의 필드를 모두 가지고 있는 상태)
# DTO와 비슷한 기능
class PhotoForm(forms.ModelForm):
    # 무조건 Meta 선언(상속받는 모델이 어떤 건지 선언)
    class Meta:
        model = Photo
        fields = "__all__"
