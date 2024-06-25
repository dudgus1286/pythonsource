from django.db import models


# 테이블과 동일한 모델 정의
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # auto_now_add : 새글 등록 시 자동 날짜 기입
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    # java의 toString()과 같은 역할
    def __str__(self) -> str:
        return self.title
