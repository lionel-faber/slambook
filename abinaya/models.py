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
    sharing = models.TextField(max_length = 5000, blank = True, null = True)
    suggestions = models.TextField(max_length = 5000, blank = True, null = True)
    def __str__(self):
        return self.name
