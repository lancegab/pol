# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Topic
from .models import Choice
from .models import Comment


# Register your models here.
admin.site.register(Topic)
admin.site.register(Choice)
admin.site.register(Comment)
