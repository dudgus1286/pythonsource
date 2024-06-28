from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.core.paginator import Paginator
from .models import Question, Answer, Comment
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


# 비로그인 상태로 글 작성 페이지로 가면 로그인 페이지로 이동하게 함, 로그인 성공하면 글 작성 페이지로 이동
@login_required(login_url="common:login")
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # 작성자 == 로그인 유저 입력
            question.author = request.user
            question.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="common:login")
def question_delete(request, qid):
    question = get_object_or_404(Question, id=qid)
    question.delete()
    return redirect("board:question_list")


@login_required(login_url="common:login")
def question_modify(request, qid):
    # qid 에 해당하는 question 찾은 후 변경할 부분 수정 후 save
    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:question_detail", qid=qid)
    else:
        form = QuestionForm(instance=question)
    return render(request, "board/question_form.html", {"form": form})


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


def question_list(request):
    """전체 질문 추출"""
    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)

    # questions = Question.objects.all()
    questions = Question.objects.order_by("-created_at")

    paginator = Paginator(questions, 20)
    page_obj = paginator.get_page(page)

    # context = {"questions": questions}
    context = {"questions": page_obj}

    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)
    context = {"question": question}
    return render(request, "board/question_detail.html", context)


@login_required(login_url="common:login")
def comment_create_question(request, qid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = get_object_or_404(Question, id=qid)
            comment.author = request.user
            comment.save()
            # return redirect("board:question_detail", qid)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=qid),
                    comment.id,
                )
            )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:question_detail", qid=comment.question.id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=comment.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("board:question_detail", qid=comment.question.id)


@login_required(login_url="common:login")
def comment_create_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.answer = answer
            comment.author = request.user
            comment.save()
            # return redirect("board:question_detail", answer.question.id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", qid=answer.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:question_detail", comment.answer.question.id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url(
                        "board:question_detail", qid=comment.answer.question.id
                    ),
                    comment.id,
                )
            )
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("board:question_detail", qid=comment.answer.question.id)


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
