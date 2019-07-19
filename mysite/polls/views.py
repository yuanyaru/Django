from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice

# Create your views here.


def index(request):
    # 展示数据库里以发布日期排序的最近 5 个投票问题，以空格分割
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    # 载入模板
    # template = loader.get_template('polls/index.html')
    # 填充上下文
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse("Hello, World, You're at the polls index.")
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


# 投票详情视图
def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                                                     'error_message': "You didn't select a choice.",
                                                     })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

