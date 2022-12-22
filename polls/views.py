from django.http import HttpResponse
from .models import Question

def detail(request, question_id):
    return  HttpResponse("Yout looking at the Question %s" %question_id)

def results(request,  question_id):
    response = "Your Looking at the Results of Question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Your Voting on Question "%question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
