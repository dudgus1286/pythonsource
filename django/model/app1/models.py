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


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.instrument


class Album(models.Model):
    # 관계 설정(외래키), 영속성 전이
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self) -> str:
        return self.artist.first_name + ", " + self.name


class Fruit(models.Model):
    # 기본키 직접 지정(데이터 없을 때만 수정 가능)
    name = models.CharField(max_length=100, primary_key=True)
