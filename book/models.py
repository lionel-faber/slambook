# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField(max_length = 500)
    def __str__(self):
        return self.question

class Response(models.Model):
    name = models.TextField(max_length = 5000, blank = True, null = True)
    email = models.TextField(max_length = 5000, blank = True, null = True)
    phone = models.TextField(max_length = 5000, blank = True, null = True)
    dob = models.TextField(max_length = 5000, blank = True, null = True)
    t_h = models.TextField(max_length = 5000, blank = True, null = True)
    food = models.TextField(max_length = 5000, blank = True, null = True)
    song  = models.TextField(max_length = 5000, blank = True, null = True)
    fav_place = models.TextField(max_length = 5000, blank = True, null = True)
    fav_person = models.TextField(max_length = 5000, blank = True, null = True)
    jail = models.TextField(max_length = 5000, blank = True, null = True)
    invisible = models.TextField(max_length = 5000, blank = True, null = True)
    memory = models.TextField(max_length = 5000, blank = True, null = True)
    wish = models.TextField(max_length = 5000, blank = True, null = True)
    best_thing = models.TextField(max_length = 5000, blank = True, null = True)
    worst_thing = models.TextField(max_length = 5000, blank = True, null = True)
    rating = models.TextField(max_length = 5000, blank = True, null = True)
    advice = models.TextField(max_length = 5000, blank = True, null = True)
    def __str__(self):
        return self.name
