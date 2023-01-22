from .models import *
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def followToggle(request, author):
    if request.user.is_authenticated:
        authorObj = User.objects.get(username=author)
        currentUserObj = User.objects.get(username=request.user.username)
        following = authorObj.following.all()

        if author != currentUserObj.username:
            if currentUserObj in following:
                authorObj.following.remove(currentUserObj.id)
            else:
                authorObj.following.add(currentUserObj.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('app:login')

