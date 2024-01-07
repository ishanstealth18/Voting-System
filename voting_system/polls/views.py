from django.shortcuts import render
from .models import Question, Choice
import logging

logger = logging.getLogger(__name__)


# Create your views here.


def welcome_page(request):
    return render(request, "welcome.html/")


def poll_questions_page(request):
    questions_list = Question.objects.all().values()
    context = {
        'questions': questions_list,
    }
    return render(request, "poll_questions.html/", context)


def vote(request, q_id):
    # Basic queries to retrieve data from the table using filter() and get() function. filter() function always returns
    # queryset and get() function returns a single object
    choices = Choice.objects.filter(question_id=q_id).values('votes', 'choice_text')
    question = Question.objects.get(id=q_id)
    if request.method == "POST":
        # Get the data posted from the web page by using get() function
        selected_choice = request.POST.get('choice')
        # 'choice_set' function will give us single object, which can be then used to call different fields from
        # database
        # choice_vote = question.choice_set.get(choice_text=selected_choice)
        # get() function will also give same result as 'choice_set.get()'
        choice_vote = Choice.objects.get(choice_text=selected_choice)
        # Just an extra query to get a specific field from the database. In this case, its 'votes' field
        choice_data = Choice.objects.values_list('votes', flat=True).get(choice_text=selected_choice)
        # accessing 'votes' field from the database table
        choice_vote.votes += 1
        # saving the data back to database
        choice_vote.save()
        context = {
            'question': question,
            'choices': choices,
            'choice_data': choice_data,
            'choice_vote': choice_vote,
            'selected_choice': selected_choice,
        }
    else:
        context = {
            'question': question,
            'choices': choices,
        }

    return render(request, "vote.html/", context)


def results(request, q_id):
    question = Question.objects.get(id=q_id)
    choice_list = Choice.objects.filter(question_id=q_id).values().all()


    context = {
        'question': question,
        'choice_list': choice_list,
    }
    return render(request, "results.html/", context)

