#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
def home(request):
    # home page 
    courses=['课程']
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context={'courses':courses,
             'teachers':teachers}
    return render(request, "index.html", context)


def app(request):
    # tool page 
    context={}
    return render(request,"index.html",context)


def course(request,id):
    # course page 
    context={}
    course = Course.objects.get(id=id)
    questions = Question.objects.filter(course__id=id)
    teachers = Teacher.objects.filter(course=course)
    lecturer=[]
    coaches=[]
    for teacher in teachers:
        if teacher.role=='Lecturer':
            lecturer.append(teacher)
        else:
            coaches.append(teacher)
    print "teacher:",lecturer
    print "coach:",coaches
    context={'course':course,
             'questions':questions,
             'lecturers':lecturer,
             'coaches':coaches
             }
    return render(request,"course.html",context)
    