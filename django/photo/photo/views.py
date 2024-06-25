from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm


def edit(request, id):
    photo = get_object_or_404(Photo, id=id)

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("photo_detail", id=id)
    else:
        # 수정 폼이기 때문에 조회한 원본글 데이터를 같이 보냄
        form = PhotoForm(instance=photo)

    return render(request, "photo/photo_edit.html", {"form": form})


def remove(request, id):
    photo = get_object_or_404(Photo, id=id)
    photo.delete()

    return redirect("photo_list")


def detail(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, "photo/photo_detail.html", {"photo": photo})


def create(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():  # 유효성(모델 정의된 규칙)
            form.save()  # model.save() 호출
            return redirect("photo_list")
    else:
        form = PhotoForm()

    return render(request, "photo/photo_create.html", {"form": form})


def list(request):
    photos = Photo.objects.all()

    return render(request, "photo/photo_list.html", {"photos": photos})
