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
    
    # created_on_count = None
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        following_actions = user.followers.all().order_by('-id')[:15]
        contact = ContactUsForm()
        if request.method == "POST":
            contact = ContactUsForm(request.POST)
    if contact.is_valid():
            contact.save()
            return redirect('app:home')

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

