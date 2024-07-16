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
    printoski(data)
    classlvl = data.get('class_level')
    class_abbr = data.get('class_abbr')
    class_range = data.get('class_range')

    classlist = ClassList.objects.create(class_level=classlvl, class_abbr=class_abbr, class_range=class_range)
    return HttpResponseRedirect(reverse('classList'))


def printoski(data):
    print(data)