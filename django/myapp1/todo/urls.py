from django.urls import path
from . import views

urlpatterns = [
    # conpig / urls.py 에서 이미 경로를 타고 와서 path("(공백)")
    path("", views.list, name="list"),
]
