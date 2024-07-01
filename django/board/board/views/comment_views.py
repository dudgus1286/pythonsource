from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from board.models import Question, Answer, Comment
from board.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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
