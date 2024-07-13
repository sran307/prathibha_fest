from django.shortcuts import render # type: ignore
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect # type: ignore


# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')