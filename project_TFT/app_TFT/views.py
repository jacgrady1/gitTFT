from django.shortcuts import render



def home(request):
    # home page 
    courses=['我们的课程','我们的特色'，'我们的团队']
    
    context={'courses':courses,
    }
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
    else if id==2:
        context={}
    else if id==3:
        context={}    
    return render(request,"course.html",context)
    