from django.shortcuts import render # type: ignore
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect # type: ignore
from datetime import date
from .models import ClassList
from django.urls import reverse  # type: ignore

# Create your views here.


def dashboard(request):
    today_date = date.today().strftime('%d-%m-%Y')
    context = {'today_date':today_date, 'menuactive':'dashboard'}
    return render(request,'dashboard.html',context)


def quizMaster(request):
    context = {'menuactive':'quizMaster'}
    return render(request,'quiz_master.html',context)


def classList(request):
    classlists = ClassList.objects.all()
    context = {'menuactive':'classList','classlist':classlists}
    return render(request,'class_list.html',context)


def saveClasslist(request):
    data = request.POST
    classno = data.get('classno')
    class_level = data.get('class_level')
    class_level_abbr = data.get('class_level_abbr')

    addeditType = data.get('addedit')
    classid = data.get('classid')
    if(addeditType=='add'):
        ClassList.objects.create(classno=classno, class_level=class_level, class_level_abbr=class_level_abbr)
    else:
        classAvail = ClassList.objects.get(id=classid)
        classAvail.classno = classno
        classAvail.class_level = class_level
        classAvail.class_level_abbr = class_level_abbr
        classAvail.save()
    return HttpResponseRedirect(reverse('classList'))


def printoski(data):
    print(data)


