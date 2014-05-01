from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from weddingpics.models import WeddingPic
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os 
# Create your views here.

SECURE_ROOT = '/home/user/protected/'

def index(request):
    context = RequestContext(request)
    pics = WeddingPic.objects.all()
    context_dict = {'pics': pics}
    
    return render_to_response('weddingpics/index.html', context_dict, context)
def get_absolute_filename(filename='', safe=True):
    if not filename:
        return os.path.join(SECURE_ROOT, 'index')
    if safe and '..' in filename.split(os.path.sep):
        return get_absolute_filename(filename='')
    return os.path.join(SECURE_ROOT, filename)

@login_required
def retrieve_file(request, filename=''):
    abs_filename = get_absolute_filename(filename)
    response = HttpResponse() # 200 OK
    del response['content-type'] # We'll let the web server guess this.
    response['X-Accel-Redirect'] = abs_filename
    return response