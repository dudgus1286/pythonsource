from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        # 테이블명 (기본설정 앱이름_모델명) 을 지정
        # 설정한 후 makemigrations - migrate 명령문 실행
        db_table = "person"

    # makemigrations 대상 아님
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
