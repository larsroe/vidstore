from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from vidstore.video.models import Video


def listall(request):
    allvids = Video.objects.all()
    return render_to_response('viewall.html', {'videos':allvids, 'user':request.user})

def detail(request, id):
    user = request.user
    video = get_object_or_404(Video, id=id)
    return render_to_response('viewone.html', {'video':video, 'user':user})

@login_required
def rent_video(request):
    user = request.user
    video = get_object_or_404(Video, id=request.POST.get('id'))
    video.rent_video(user.username)
    messages = ["Successfully rented %s" % video.title]
    return render_to_response('viewone.html', {'video':video, 'user':user, 'messages':messages})

@login_required
def return_video(request):
    user = request.user
    video = get_object_or_404(Video, id=request.POST.get('id'))
    video.return_video(user)
    messages = ["Successfully returned %s" % video.title]
    return render_to_response('viewone.html', {'video':video, 'user':user, 'messages':messages})


