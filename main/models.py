from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
# Create your models here.
class Passage(models.Model):
    title = models.CharField(max_length=100)
    body  = models.TextField()
    time  = models.DateTimeField(timezone.now)
    changetime = models.DateTimeField(timezone.now,blank=True,null=True)
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
