import json

from django.db import models
from django.utils import timezone
from django.urls import reverse


class Action(models.Model):
    action_name = models.CharField(max_length=20)
    creation_date = models.DateTimeField(default=timezone.now)  # Not to call function, server will call on run

    def get_current_count(self):
        current_count = self.instance_set.count()
        return current_count

    def get_last(self):
        current_count = self.instance_set.last()
        return current_count

    def to_json(self):
        action_dict = {
            self.action_name: {
                "creation_date": self.creation_date.timestamp(),
                "current_count": self.get_current_count()
            }
        }
        return json.dumps(action_dict)

    def get_absolute_url(self):
        return reverse('bizint:info', args=[str(self.id)])

    def __str__(self):
        return self.action_name


class Instance(models.Model):
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default=0)
    up_date = models.DateTimeField('date updated', default=timezone.now) # Not to call function, server will call on run
    note = models.CharField(default="", max_length=200)

    def __str__(self):
        return str(self.count)

