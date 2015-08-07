#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
def home(request):
    # home page 
    courses=['课程']
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    lecturers=[]
    coaches=[]
    for teacher in teachers:
        if teacher.role=='Lecturer':
            lecturers.append(teacher)
        else:
            coaches.append(teacher)
    print "teacher:",len(lecturers)
    context={'courses':courses,
             'lecturers':lecturers}
    return render(request, "index.html", context)


def course(request,id):
    # course page 
    context={}
    course = Course.objects.get(id=id)
    questions = Question.objects.filter(course__id=id)
    teachers = Teacher.objects.filter(course=course)
    lecturers=[]
    coaches=[]
    for teacher in teachers:

        if teacher.role=='Lecturer':
            lecturers.append(teacher)

        else:
            coaches.append(teacher)
    print "lecturers:",lecturers
    #print "coach:",coaches

    lectures = Lecture.objects.filter(course__id=id)
    #print lectures
    for lecture in lectures:
       print lecture.chapter_set.all()

    context={'course':course,
             'questions':questions,
             'lecturers':lecturers,
             'coaches':coaches,
             'lectures':lectures
             }
    return render(request,"course.html",context)


def course_register(request,id):
    # currently course_register is the same with course page.
    context={}
    course = Course.objects.get(id=id)
    print course
    context={'course':course}
    return render(request,"course_register.html",context)

