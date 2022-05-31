from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("Você está vendo a questão %s." % question_id)
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "Você está vendo os resultados da questão %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s." % question_id)
    