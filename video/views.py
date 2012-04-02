from django.http import HttpResponse
from django.shortcuts import render_to_response
from vidstore.video.models import Video
import pprint

def listall(request):
    allvids = Video.objects.all()
    return render_to_response('viewall.html', {'videos':allvids})

def detail(request):
#TODO: Fill in video
    return render_to_response('viewone.html')

def rent(request):
    try:
        video = Video.objects.get(id=request.POST['id'])
        print "video is %s" % video
        video.checkoutVideo(request.META['USER'])
        video.save()
        return render_to_response('viewone.html', {'video':video})
    except KeyError:
        return render_to_response('viewone.html', {})


