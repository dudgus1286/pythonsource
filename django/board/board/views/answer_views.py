from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from board.models import Question, Answer
from board.forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url="common:login")
def answer_create(request, qid):
    question = get_object_or_404(Question, id=qid)
    """답변 등록"""

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # commit = False : DB 반영 X
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페이지 특정 위치로 지정
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:question_detail", qid=qid), answer.id
                )
            )
        else:
            form = AnswerForm()

    # forms.py 로 폼 기능 구현 안 한 경우
    # answer = Answer.objects.create(
    #     question=question, content=request.POST.get("content")
    # )

    # 답변 등록하는 다른 방법 1
    # answer = question.answer_set.create(content=request.POST.get("content"))
    # 2
    # answer = Answer(question=question, content=request.POST.get("content"))
    # # 객체 생성하는 방식은 save() 필수
    # answer.save()

    # 등록 실패 시에는 get 방식으로 처리해야 함
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


def answer_modify(request, aid):
    # 수정 성공 시 detail로
    answer = get_object_or_404(Answer, id=aid)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            # return redirect("board:question_detail", qid=answer.question.id)
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:question_detail", qid=answer.question.id),
                    answer.id,
                )
            )
    else:
        form = AnswerForm(instance=answer)
    return render(request, "board/answer_form.html", {"form": form})


def answer_delete(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    qid = answer.question.id
    answer.delete()
    # question id 필요
    return redirect("board:question_detail", qid=qid)
