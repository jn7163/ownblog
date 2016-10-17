from django.shortcuts import render
from models import Passage,Comment,Accessamount,UpdataFile
from django.utils import timezone
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import os
MEDIA_URL = '/media/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Create your views here.
def getIPFromDJangoRequest(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']

def addaccessamount(request,pid):
    if not request.user.is_authenticated():
        try:
            accessamount=Passage.objects.get(id=pid).accessamount
        except:
            return 0
        accessamount.amount+=1
        accessamount.save()
def check(string):
    if string=='':
        return 'none'
    elif string.find('<script') != -1:
        return 'script'
    else:
        return 'ok'

def index(request,page=1):
    passages=Passage.objects.order_by('-time')[(int(page)-1)*6:int(page)*6]
    context={
        'passages':passages,    	
    }
    return render(request,'index.html',context)

def passages(request,page):
    pinpagenum=10#passage in pages num
    passages=Passage.objects.order_by('-time')[(int(page)-1)*pinpagenum:int(page)*pinpagenum]
    allpassagenum=Passage.objects.count()
    allpagenum=int(allpassagenum)/pinpagenum+1
    if range(1,int(page))[5:]:
        betweenpagesbefore = range(1,int(page))[5:]
    else:
        betweenpagesbefore = range(1,int(page))
    betweenpagesnext = range(int(page)+1,allpagenum+1)[:5]
    context={
        'passages':passages,
        'allpagenum':allpagenum,
        'page':page,
        'betweenpagesbefore':betweenpagesbefore,
        'betweenpagesnext':betweenpagesnext,
    }
    if int(page)>1:
        context['beforepage']=int(page)-1
    if int(page)<allpagenum:
        context['nextpage']=int(page)+1
    return render(request,'passages.html',context)

def passage1(request,pid):
    return passage(request,pid,1)

def passage(request,pid,commentpage):
    commentinpage=5
    context2={}
    addaccessamount(request,pid)
    passage=Passage.objects.get(id=pid)
    if request.method=="POST":        
        comment=Comment()
        comment.time=timezone.now()
        comment.passage=passage
        comment.ip=getIPFromDJangoRequest(request)
        comment.body=request.POST['body']
        if request.POST.get('ifhideip')=='on':
            comment.ifhideip=True
        else:
            comment.ifhideip=False
        if request.POST.get('ifsafe')=='on':
            comment.ifsafe=True            
        else:
            comment.ifsafe=False
        result = check(request.POST.get('body')) 
        print result                                             
        if result=='ok':
            comment.save()
        elif result=='none':
            context2['error']='none' 
            context2 = dict(context2.items()+request.POST.items()) 
            print context2             
        elif result=='script':
            if comment.ifsafe: 
                context2['error']='script'
                context2 = dict(context2.items()+request.POST.items())
            else:
                comment.save()     
        else:
            pass        
    comments=passage.comment_set.order_by('-time')[(int(commentpage)-1)*commentinpage:int(commentpage)*commentinpage]
    allpassagenum=passage.comment_set.count()
    allpagenum=int(allpassagenum)/commentinpage+1
    if range(1,int(commentpage))[5:]:
        betweenpagesbefore = range(1,int(commentpage))[5:]
    else:
        betweenpagesbefore = range(1,int(commentpage))
    betweenpagesnext = range(int(commentpage)+1,allpagenum+1)[:5]
    context={
        'passage':passage,
        'comments':comments,
        'page':commentpage,
        'allpagenum':allpagenum,
        'betweenpagesbefore':betweenpagesbefore,
        'betweenpagesnext':betweenpagesnext,
    }
    if context2.items():
        context=dict(context.items()+context2.items())
    if int(commentpage)>1:
        context['beforepage']=int(commentpage)-1
    if int(commentpage)<allpagenum:
        context['nextpage']=int(commentpage)+1
    return render(request,'passage.html',context)


def about(request):
    return render(request,'about.html',{})
def add(request):
    if request.user.is_authenticated():
        if request.method=="POST":
            passage=Passage()
            passage.title = request.POST['title']
            passage.body = request.POST['body']
            passage.time = timezone.now()
            passage.info = request.POST.get('info')
            passage.save()

            accessamount = Accessamount()
            accessamount.passage = passage
            accessamount.amount=0
            accessamount.save()
            return HttpResponseRedirect("/"+str(passage.id))
        return render(request,'add.html')
    else:
        return HttpResponseRedirect("/")

def addfile(request):
    if request.user.is_authenticated():
        if request.method=='POST':
            f = request.FILES.get('file',None)
            if f:
                updatafile = UpdataFile()
                updatafile.name = f.name
                updatafile.save()
                savename = str(updatafile.id)+'.'+f.name.split(".")[-1]  
                dest = open(os.path.join(MEDIA_ROOT, savename),'wb+')
                dest.write(f.read())
                dest.close()
                updatafile.url=os.path.join(MEDIA_URL, savename)
                print updatafile.url
                updatafile.save()
                return HttpResponseRedirect("/files")
            else:
                return render(request,'addfile.html',{'error':'none',})
        else:
            return render(request,'addfile.html')
    else:
        return HttpResponseRedirect("/")


def files(request):
    files=UpdataFile.objects.all().order_by('-id')
    return render(request,'files.html',{'files':files})
def change(request,pid):
    if request.user.is_authenticated():
        passage=Passage.objects.get(id=pid)
        if request.method=='POST':
            passage.title = request.POST['title']
            passage.body = request.POST['body']
            passage.info = request.POST.get('info')
            passage.changetime = timezone.now()
            passage.save()
            return HttpResponseRedirect("/"+str(pid))
        else:          
            return render(request,'change.html',{'passage':passage})
    else:
        return HttpResponseRedirect("/")