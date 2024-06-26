from django.db import models


class Question(models.Model):
    # verbose_name : 주석, 라벨 기능
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    # auto_now_add : 가장 처음 삽입시에만 날짜와 시간 삽입
    # auto_now : 수정할 때마다 날짜와 시간 삽입
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")

    def __str__(self):
        return self.content
