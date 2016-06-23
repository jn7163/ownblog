from django.contrib import admin
from .models import Passage,Comment,Accessamount,UpdataFile
# Register your models here.
admin.site.register(Passage)
admin.site.register(Comment)
admin.site.register(Accessamount)
admin.site.register(UpdataFile)