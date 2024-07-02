from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse


def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content").strip()

        Comment.objects.create(user=request.user, post=post, content=content)
        return redirect("blog:detail", post_id)
    return redirect("blog:detail", post_id)


def delete(request, post_id):
    get_object_or_404(Post, id=post_id).delete()
    return redirect("blog:list")


@login_required(login_url="common:login")
def modify(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:detail", post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/modify.html", {"form": form, "post": post})


@login_required(login_url="common:login")
def create(request):
    if request.method == "POST":
        # 폼에 post로 넘어오는 내용 담기
        # request.POST : 일반 내용, request.FILES : 파일 내용
        form = PostForm(request.POST, request.FILES)
        # 폼 유효성 검증
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # 태그 저장
            form.save_m2m()

            # 리스트로 이동
            return redirect("blog:list")
            # return redirect("blog:detail", post.id)
    else:
        form = PostForm()
    return render(request, "blog/create.html", {"form": form})


def list(request):
    # 전체 포스트 조회
    page = request.GET.get("page", 1)

    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page)

    context = {"posts": page_obj}
    return render(request, "blog/list.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 로그인 유저의 좋아요 여부 확인
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {"post": post, "is_liked": is_liked}
    return render(request, "blog/post.html", context)


def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    is_liked = post.likes.filter(id=request.user.id).exists()
    is_liked_change = False

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        is_liked_change = True

    return JsonResponse({"likes": post.likes.count(), "is_liked": is_liked_change})
