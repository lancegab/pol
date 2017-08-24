# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from django.views import generic

from .models import Topic
from .models import Choice


# Create your views here.
# def index(request):
#     all_topics = Topic.objects.all();
#
#     return render(request, "poll/index.html", {'all_topics' : all_topics})
#
# def detail(request, topic_id):
#     topic   = get_object_or_404(Topic, pk = topic_id)
#     choices =  get_list_or_404(Choice, topic_id = topic_id)
#
#     return render(request, "poll/detail.html",
#         {
#             'topic'  : topic,
#             'choices': choices
#         })
#
# def results(request, topic_id):
#     topic = get_object_or_404(Topic, pk = topic_id)
#     return render(request, 'poll/results.html', {'topic': topic})

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        """Return the last five published topics."""
        return Topic.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Topic
    template_name = 'poll/detail.html'


class ResultsView(generic.DetailView):
    model = Topic
    template_name = 'poll/results.html'


def vote(request, topic_id):
    topic =  get_object_or_404(Topic, pk = topic_id)
    try:
        selected_choice = topic.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the topic voting form.
        return render(request, 'poll/detail.html', {
            'topic': topic,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(topic.id,)))
