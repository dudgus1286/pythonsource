from django.shortcuts import render
from django.http import HttpResponse


# def list(request):
#     """
#     일반 문자열 응답
#     """
#     return HttpResponse("Hello")


def list(request):
    """
    html 응답
    """
    return render(request, "todo/todo_list.html")
