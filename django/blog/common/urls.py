from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = "common"

urlpatterns = [
    path("register/", views.register, name="register"),
    # login 처리를 하는 뷰가 함수형 뷰가 아니라 클래스뷰임
    # 클래스뷰는 함수형처럼 사용하려면 as_view() 사용
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="common/login.html",
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # 기존 비밀번호 변경 후 세션 값 다시 담아줌
    # 비밀번호 초기화
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="common/password_change.html",
            # 비밀번호 성공 시 이동 경로(기본값-password_chane_done)
            success_url=reverse_lazy("common:login"),
        ),
        name="password_change",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="common/password_reset.html",
            email_template_name="common/password_reset_email.txt",
            success_url=reverse_lazy("common:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="common/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="common/password_reset_confirm.html",
            success_url=reverse_lazy("common:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="common/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
