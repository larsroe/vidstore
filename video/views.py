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
        return render_to_response('viewone.html', locals())

def rentVideo(request):
    user = request.user
    try:
        #TODO: Ensure that it is not already checked out
        video = Video.objects.get(id=request.POST['id'])
        print "user is %s" % user.username
        video.checkoutVideo(user.username)
        status_message = "Successfully rented %s" % video.title
        operation_success = True
        return render_to_response('viewone.html', locals())
    except KeyError:
        status_message = "Could not rent %s" % video.title
        return render_to_response('viewone.html', locals())

def returnVideo(request):
    user = request.user
    try:
        #TODO: Ensure that it user is the same one who has it checked out
        video = Video.objects.get(id=request.POST['id'])
        video.returnVideo()
        status_message = "Successfully returned %s" % video.title
        operation_success = True
        return render_to_response('viewone.html', locals())
    except KeyError:
        status_message = "Unable to return %s" % video.title
        return render_to_response('viewone.html', locals())


