from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout, get_user_model
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.db.models import Avg
from django.views import generic
from django.urls import reverse 
from django.db.models import Q
from .models import *
User = get_user_model()

def home(request):

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

def results(request):
    search = None
    users = None
    charts = None
    user_count = 0
    chart_count = 0
    if 'q' in request.GET:
        search = request.GET['q']
        user_search = Q(Q(username__icontains=search))
        chart_search = Q(Q(slug__icontains=search))
        users = User.objects.filter(user_search)
        charts = Chart.objects.filter(chart_search)
        user_count = users.count()
        chart_count = charts.count()
    if search==None or len(search) < 3: # bitta harf bilan qidirmaslig uchun
        return redirect('app:home')
    context={
        "users":users,
        "charts":charts,
        "user_count":user_count,
        "chart_count":chart_count,
        "search":search
    }
    return render(request, "pages/result.html", context)

def ProfileView(request, username):
        user_p = User.objects.get(username=username)
        author = get_object_or_404(User, username=username)
        return render(request, 'pages/profile.html')
