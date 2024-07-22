from django.shortcuts import render # type: ignore
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect # type: ignore
from datetime import date
from .models import ClassList,QuizMaster
from django.urls import reverse  # type: ignore
from django.utils import timezone # type: ignore

# Create your views here.


def dashboard(request):
    today_date = date.today().strftime('%d-%m-%Y')
    context = {'today_date':today_date, 'menuactive':'dashboard'}
    return render(request,'dashboard.html',context)


def quizMaster(request):
    classlist = ClassList.objects.values('class_level_abbr').distinct()
    context = {'menuactive':'quizMaster', 'classlist':classlist}
    return render(request,'quiz_master.html',context)

def quiztonList(request):
    quizton = QuizMaster.objects.all()
    context = {'quizton':quizton}
    return render(request,'quizton_list.html',context)

def saveQuizton(request):
    try:
        classLevel = request.POST.get('classLevel')
        image = request.FILES.get('inputImage')
        audio = request.FILES.get('inputAudio')
        video = request.FILES.get('inputVideo')

        QuizMaster.objects.create(classLevel=classLevel,image_Q=image,audio_Q=audio,video_Q=video, updated_on = timezone.now())
        return JsonResponse({'status':200, 'msg':"Added successfully"})
    except Exception as e:
        return JsonResponse({'status':300, 'msg':"Some error occurred"})


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


