from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.loader import render_to_string

from quiz.multichoice.models import MCQuestion
from quiz.multichoice.forms import MCQuestionForm
from quiz.models import Quiz
from quiz.forms import NewQuizForm


@login_required
def add_mcquestion(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.user != quiz.created_by:
        c = RequestContext(request)
        return render(request, 'quiz/permission_error.html',
                      {'page_name': "Permission Error",
                       'action':
                       'add a question to a quiz you did not create,',
                       'quiz': quiz},
                      # context=c
                      )

    else:  # user is the creator
        #c = RequestContext(request)
        if request.method == "POST":
            form = MCQuestionForm(request.POST)
            form.inquiz = quiz_id
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/quizlist/")
            else:
                return render(request, "multichoice/add_question.html", {'formset': form, 'quiz': quiz})
        else:  # new blank form
            form = MCQuestionForm()
        # stuff
            #c = RequestContext(request)
            return render(request, "multichoice/add_question.html", {'formset': form, 'quiz': quiz})


# def question_list(request):
#    questions = MCQuestion.objects.all()
# return render(request, 'quiz/list_question.html', {'questions':
# questions})
