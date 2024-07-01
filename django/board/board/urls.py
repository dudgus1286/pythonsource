from django.urls import path

# from . import views
from .views import base_views, question_views, answer_views, comment_views, vote_views

# url패턴 이름이 중복될 경우 구별되게 앱네임 지정
app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", base_views.question_list, name="question_list"),
    # http://127.0.0.1:8000/board/2
    path("<int:qid>/", base_views.question_detail, name="question_detail"),
    # http://127.0.0.1:8000/board/question/create
    path("question/create/", question_views.question_create, name="question_create"),
    # http://127.0.0.1:8000/board/question/modify/2
    path(
        "question/modify/<int:qid>/",
        question_views.question_modify,
        name="question_modify",
    ),
    # http://127.0.0.1:8000/board/question/delete/2
    path(
        "question/delete/<int:qid>/",
        question_views.question_delete,
        name="question_delete",
    ),
    #
    # 답변
    # http://127.0.0.1:8000/board/answer/create/2 (답변이 달리는 질문 번호)
    path("answer/create/<int:qid>/", answer_views.answer_create, name="answer_create"),
    # http://127.0.0.1:8000/board/answer/modify/3 (수정하려는 답변 번호)
    path("answer/modify/<int:aid>/", answer_views.answer_modify, name="answer_modify"),
    # http://127.0.0.1:8000/board/answer/delete/3
    path("answer/delete/<int:aid>/", answer_views.answer_delete, name="answer_delete"),
    #
    # 댓글
    # http://127.0.0.1:8000/board/comment/create/question/4
    path(
        "comment/create/question/<int:qid>/",
        comment_views.comment_create_question,
        name="comment_create_question",
    ),
    # http://127.0.0.1:8000/board/comment/modify/question/6
    path(
        "comment/modify/question/<int:cid>/",
        comment_views.comment_modify_question,
        name="comment_modify_question",
    ),
    # http://127.0.0.1:8000/board/comment/delete/question/6
    path(
        "comment/delete/question/<int:cid>/",
        comment_views.comment_delete_question,
        name="comment_delete_question",
    ),
    #
    # http://127.0.0.1:8000/board/comment/create/answer/4
    path(
        "comment/create/answer/<int:aid>/",
        comment_views.comment_create_answer,
        name="comment_create_answer",
    ),
    # http://127.0.0.1:8000/board/comment/modify/answer/4
    path(
        "comment/modify/answer/<int:cid>/",
        comment_views.comment_modify_answer,
        name="comment_modify_answer",
    ),
    # http://127.0.0.1:8000/board/comment/delete/answer/4
    path(
        "comment/delete/answer/<int:cid>/",
        comment_views.comment_delete_answer,
        name="comment_delete_answer",
    ),
    #
    # 추천
    # http://127.0.0.1:8000/board/vote/question/1 : 질문추천
    path("vote/question/<int:qid>/", vote_views.vote_question, name="vote_question"),
    # http://127.0.0.1:8000/board/vote/answer/3 : 답변추천
    path("vote/answer/<int:aid>/", vote_views.vote_answer, name="vote_answer"),
]
