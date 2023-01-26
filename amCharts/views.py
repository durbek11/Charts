from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    charts_count = Chart.objects.count()
    user_count = User.objects.count()
    date_joined_count = User.objects.filter(date_joined__date=timezone.now()-timezone.timedelta(0)).count()
    users = User.objects.all().order_by('-id')[:date_joined_count]
    elem_count = Element.objects.count()
    following_actions = None
    # created_on_count = None
    return render(request, 'pages/home.html')

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    
    return render(request, 'registration/signup.html', {"form":form})

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

