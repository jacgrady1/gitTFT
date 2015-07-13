#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    # home page 
    courses=['课程']
    context={}

    return render(request, "index.html", context)


def app(request):
    # tool page 
    context={}
    return render(request,"index.html",context)


def course(request,id):
    # course page 
    context={}
    if id==1:
        context={}
    if id==2:
        context={}    
    return render(request,"course.html",context)
    