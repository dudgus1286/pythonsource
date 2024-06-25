from django.db import models


class Photo(models.Model):
    # CharField : 화면단에서 input:text 로 받음, 크기 지정해야 함
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    # TextField : 화면단에서 textarea 로 받음, 크기 지정 필요없음
    description = models.TextField()
    price = models.IntegerField()

    # admin Photo 모델 페이지에서 제목으로 출력됨
    def __str__(self) -> str:
        return self.title
