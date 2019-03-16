from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect

from .models import Action, Instance


def index(request):
    actions = Action.objects.all()
    context = {
        "action_list": actions,
    }
    return render(request, 'bizint/index.html', context)


def info(request, action_id):
    action = get_object_or_404(Action, pk=action_id)
    context = {
        "action": action,
    }
    return render(request, 'bizint/info.html', context)


## PROTOTYPE ##
def add(request, action_id):
    action = get_object_or_404(Action, pk=action_id)
    action.instance_set.create(action=action, count=action.get_current_count() + 1)

    return redirect(action.get_absolute_url())


def api_actions(request):
    actions = Action.objects.all()
    x = [action.to_json() for action in actions]

    context = {
        "action_list": actions,
    }
    return HttpResponse(x)


def api_action(request, action_id):
    pass