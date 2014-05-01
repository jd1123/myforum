from django.contrib import admin
from weddingpics.models import WeddingPic, WeddingPicAdmin

# Register your models here.
admin.site.register(WeddingPic, WeddingPicAdmin)