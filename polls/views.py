from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by("-pub_date")[:5]


# def index(request):
#     latest_question_list = Question.objects.order_by("pub_date")
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "index.html", context)


class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question": question}
#     return render(request, "detail.html", context)


class ResultsView(generic.DetailView):
    model = Question
    template_name = "results.html"


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question": question}
#     return render(request, "results.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Dentro de request hay un objeto post con los parametros que se le han pasado
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {"question": question, "error_message": "You didn't select a choice"}
        return render(request, "detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
