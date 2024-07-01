from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from board.models import Question, QuestionCount
from django.db.models import Q, Count  # or 조건으로 데이터 조회
from board.tools.utils import get_client_ip


def question_list(request):
    """전체 질문 추출"""
    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)
    # 검색어 가져오기
    keyword = request.GET.get("keyword", "")
    # 정렬기준 가져오기
    so = request.GET.get("so", "")

    # questions = Question.objects.all()
    # questions = Question.objects.order_by("-created_at")

    if so == "recommend":
        # Question_voter 테이블이 Question 테이블과 분리되어 있어서 먼저 num_vote 이름으로 기준이 될 임시 테이블 만듦
        questions = Question.objects.annotate(num_vote=Count("voter")).order_by(
            "-num_vote", "-created_at"
        )
    elif so == "popular":
        questions = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-created_at"
        )
    else:
        questions = Question.objects.order_by("-created_at")

    if keyword:
        questions = questions.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    paginator = Paginator(questions, 10)
    page_obj = paginator.get_page(page)

    # context = {"questions": questions}
    context = {"questions": page_obj, "page": page, "keyword": keyword}

    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 클라이언트 ip 가져오기
    ip = get_client_ip(request)
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        # QuestionCount 객체 생성 후 저장
        QuestionCount(ip=ip, question_id=question.id).save()

        # Question view_cnt + 1
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)
    # 검색어 가져오기
    keyword = request.GET.get("keyword", "")
    # 정렬기준 가져오기
    so = request.GET.get("so", "recent")

    context = {"question": question, "page": page, "keyword": keyword, "so": so}
    return render(request, "board/question_detail.html", context)
