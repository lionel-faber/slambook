# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'abinaya/index.html', {"questions": questions})

def submit(request):
    name = request.POST.get('6')
    email = request.POST.get('7')
    phone = request.POST.get('8')
    dob = request.POST.get('9')
    sharing = request.POST.get('10')
    suggestions = request.POST.get('11')
    response = Response(name = name, email = email, phone = phone, dob = dob, sharing = sharing, suggestions = suggestions)
    response.save()
    return render(request, 'abinaya/thankyou.html')

@login_required(login_url="/accounts/login/")
def responselist(request):
    responses = Response.objects.all()
    return render (request, 'abinaya/responselist.html', {"responses": responses })

@login_required(login_url="/accounts/login/")
def viewresponse(request):
    sender = request.POST.get('sender')
    r = Response.objects.get(id = sender)
    return render(request, 'abinaya/response.html', {"response": r})
