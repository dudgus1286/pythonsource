from django.db import models
from django.contrib.auth.models import User


# 댓글


class Question(models.Model):
    # verbose_name : 주석, 라벨 기능
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # auto_now_add : 가장 처음 삽입시에만 날짜와 시간 삽입
    # auto_now : 수정할 때마다 날짜와 시간 삽입
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")

    # 추천 기능(그냥 하면 에러남 author 와 같은 모델을 중복해서 보기 때문에)
    # , related_name='voter_question' 지정 필요
    voter = models.ManyToManyField(User, related_name="voter_question")

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    voter = models.ManyToManyField(User, related_name="voter_answer")

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, blank=True
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content
