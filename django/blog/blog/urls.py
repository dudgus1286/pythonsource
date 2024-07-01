from django.urls import path, include
from django.views.generic import RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.list, name="list"),
    path("post/<int:post_id>/", views.detail, name="detail"),
    path("post/create/", views.create, name="create"),
    path("post/modify/<int:post_id>", views.modify, name="modify"),
    path("post/delete/<int:post_id>", views.delete, name="delete"),
]
