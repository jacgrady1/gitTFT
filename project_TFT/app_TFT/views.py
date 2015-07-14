#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
def home(request):
    # home page 
    courses=['课程']
    courses = Course.objects.all()
    context={'courses':courses}
    return render(request, "index.html", context)


def app(request):
    # tool page 
    context={}
    return render(request,"index.html",context)


def course(request):
    # course page 
    context={}
    return render(request,"course.html",context)
    