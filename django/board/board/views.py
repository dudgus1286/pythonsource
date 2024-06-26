from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


def answer_create(request, qid):
    question = get_object_or_404(Question, id=qid)
    """답변 등록"""

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # commit = False : DB 반영 X
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("board:question_detail", qid=qid)
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
