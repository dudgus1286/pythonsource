from django.urls import path
from . import views

# url패턴 이름이 중복될 경우 구별되게 앱네임 지정
app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", views.question_list, name="question_list"),
    # http://127.0.0.1:8000/board/2
    path("<int:qid>/", views.question_detail, name="question_detail"),
    # http://127.0.0.1:8000/board/question/create
    path("question/create/", views.question_create, name="question_create"),
    # http://127.0.0.1:8000/board/answer/create/2 (답변이 달리는 질문 번호)
    path("answer/create/<int:qid>/", views.answer_create, name="answer_create"),
]
