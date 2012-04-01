from django.http import HttpResponse
from django.shortcuts import render_to_response
from vidstore.video.models import Video

def listall(request):
    allvids = Video.objects.all()
    return render_to_response('viewall.html', {'videos':allvids})

def detail(request):
#TODO: Fill in video
    return render_to_response('viewone.html')


