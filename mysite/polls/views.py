from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.template import loader

from .models import Question, Choice


def indexes(request):
    latest_question_list = Question.objects.order_by("-pub_date")[0:8]
    context = {"latest_question_lis": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def question(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        pub_date = request.POST['pub_date']
        questio = Question(question_text = question_text, pub_date = pub_date)
        questio.save()
        return HttpResponse("Question saved")
    return render(request, 'polls/question.html')


def choice(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        
        id = request.POST.get('question')
        selected_question = 0
        for question in questions:
            if question.id == int(id):
                selected_question = question

        choice = request.POST['choice']
        new_choice = Choice(question = selected_question, choice_text = choice, votes = 0)
        new_choice.save()
        return HttpResponse('Choice added succesfully')
    return render(request, 'polls/choice.html', {"questions": questions})


# def indexes(request):
    # return render(request, 'polls/index.html')

# Create your views here.
