#encoding:utf-8
#from django.shortcuts import render
from main.models import Passage,Comment,Accessamount,UpdataFile
from django.http import HttpResponse
# Create your views here.
import json

@csrf_exempt
def getpassages(request):
    if request.method=="GET":
        begin = int(request.GET.get('begin','0'))
        end = int(request.GET.get('end','0'))
        passages = Passage.objects.all()[begin:end]
        return HttpResponse(json.dumps(passages))
