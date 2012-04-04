from django.http import HttpResponse
from django.shortcuts import render_to_response
from vidstore.video.models import Video
import pprint

def listall(request):
    allvids = Video.objects.all()
    return render_to_response('viewall.html', {'videos':allvids, 'user':request.user})

def detail(request, id):
    user = request.user
    try:
        video = Video.objects.get(id=id)
        return render_to_response('viewone.html', locals())
    except KeyError:
        errors = ["Could not retrieve video details"]
        return render_to_response('viewone.html', locals())

def rent_video(request):
    user = request.user
    try:
        video = Video.objects.get(id=request.POST['id'])
        video.rent_video(user.username)
        messages = [ "Successfully rented %s" % video.title ]
        return render_to_response('viewone.html', locals())
    except KeyError:
        errors = ["Could not rent %s" % video.title ]
        return render_to_response('viewone.html', locals())

def return_video(request):
    user = request.user
    try:
        video = Video.objects.get(id=request.POST['id'])
        video.return_video(user)
        messages = ["Successfully returned %s" % video.title]
        return render_to_response('viewone.html', locals())
    except KeyError:
        errors = ["Unable to return %s" % video.title]
        return render_to_response('viewone.html', locals())


