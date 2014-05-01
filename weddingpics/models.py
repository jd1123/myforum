from django.db import models
from django.contrib import admin

# Create your models here.

class WeddingPic(models.Model):
    pic = models.CharField(max_length=100)
    caption = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.pic
    
class WeddingPicAdmin(admin.ModelAdmin):
    list_display = ['pic', 'caption' ]
    search_fields = ['pic', 'caption']