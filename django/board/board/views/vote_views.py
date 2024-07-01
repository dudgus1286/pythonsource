from django.shortcuts import redirect, get_object_or_404
from board.models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="common:login")
def vote_question(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 내가 작성한 글은 추천 못하게 막기
    if request.user == question.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)
    return redirect("board:question_detail", qid)


@login_required(login_url="common:login")
def vote_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)

    if request.user == answer.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    return redirect("board:question_detail", answer.question.id)
