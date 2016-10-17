from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
# Create your models here.
class Passage(models.Model):
    title = models.CharField(max_length=100)
    body  = models.TextField()
    time  = models.DateTimeField(timezone.now)
    changetime = models.DateTimeField(timezone.now,blank=True,null=True)
    #thefile = models.FileField(upload_to = 'media/', blank=True,default='')
    info  = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return smart_unicode(self.title)

class Comment(models.Model):
    passage = models.ForeignKey('Passage')
    ifhideip = models.BooleanField(default=True)
    ifsafe = models.BooleanField(blank=True,default=False)
    ip = models.CharField(max_length=20)
    body = models.TextField()
    time = models.DateTimeField(timezone.now)
    def __unicode__(self):
        return smart_unicode(self.ip)

class Accessamount(models.Model):
    passage = models.OneToOneField('Passage')
    amount = models.IntegerField()
    def __unicode__(self):
        return smart_unicode(self.passage)

class UpdataFile(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20,blank=True)
    def __unicode__(self):
        return smart_unicode(self.name)

#
#function toStringNum(num){var str=num.toString();var addchar="";for(var i = 0;i<4-str.length;i++){addchar +="0";}return addchar+num.toString();}
# for(var i =0;1<=9999;i++){
#     strnum= toStringNum(i);
#     send(strnum);
# }
# function send(msg){$.get("https://xdmsc_recruit.leanapp.cn/final?code="+msg,function(req){console.log(req);});}