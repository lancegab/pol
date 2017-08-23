# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_text  = models.CharField(max_length=150)
    pub_date    = models.DateTimeField('date added')

    def __str__(self):
        return self.name

class Entry(models.Model):
    entry_text  = models.CharField(max_length=150)
    topic       = models.ForeignKey(Topic, on_delete = models.CASCADE)
    votes       = models.IntegerField(default=0)
    pub_date    = models.DateTimeField('date added')

    def __str__(self):
        return self.name
