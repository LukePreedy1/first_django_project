from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'quetions': question})


def results(request, question_id):
    return HttpResponse()


def vote(request, question_id):
    return HttpResponse()


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
