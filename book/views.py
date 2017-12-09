# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from book.models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'book/index.html', {"questions": questions})

def submit(request):
    name = request.POST.get('1')
    email = request.POST.get('2')
    phone = request.POST.get('3')
    dob = request.POST.get('4')
    t_h = request.POST.get('5')
    food = request.POST.get('6')
    song  = request.POST.get('7')
    fav_place = request.POST.get('8')
    fav_person = request.POST.get('9')
    jail = request.POST.get('10')
    invisible = request.POST.get('11')
    memory = request.POST.get('12')
    wish = request.POST.get('13')
    best_thing = request.POST.get('14')
    worst_thing = request.POST.get('15')
    rating = request.POST.get('16')
    advice = request.POST.get('17')
    response = Response(name = name, email = email, phone = phone, dob = dob, t_h = t_h, food = food, song = song, fav_place = fav_place, fav_person = fav_person, jail = jail, invisible = invisible, memory = memory, wish = wish, best_thing = best_thing, worst_thing = worst_thing, rating = rating, advice = advice)
    response.save()
    return render(request, 'book/thankyou.html')

@login_required(login_url='/admin')
def responselist(request):
    responses = Response.objects.all()
    return render (request, 'book/responselist.html', {"responses": responses })

@login_required(login_url='/admin')
def viewresponse(request):
    sender = request.POST.get('sender')
    r = Response.objects.get(id = sender)
    print r
    return render(request, 'book/response.html', {"response": r})
