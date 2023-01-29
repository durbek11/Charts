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
from .form import *
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


def logoutView(request):
    logout(request)
    return redirect("app:home")

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
def NewChartView(request):
    user_p = User.objects.get(username=request.user)
    user = User.objects.get(username=request.user)
    author = get_object_or_404(User, username=request.user)
    dash = author.chart.all()
    new_dash = None
    NewChart = ChartFrom()
    if request.method == 'POST':
        NewChart = ChartFrom(data=request.POST)
        if NewChart.is_valid():
            new_dash = NewChart.save(commit=False)
            new_dash.author = author
            new_dash.save()
            slug = NewChart.cleaned_data.get('slug')
            return redirect("app:chart", slug) 
   
    context={
        "NewChart":NewChart,
    }
    return render(request, "pages/new.html", context)
def ChartView(request, slug):
    chart = Chart.objects.get(slug=slug)
    post = get_object_or_404(Chart, slug=slug)
    elements = post.element.all()
    elements_count = post.element.count()
    number_avg = post.element.aggregate(Avg("value"))
    new_element= None
    # add element form
    if request.method == 'POST':
        comment_form = ElementForm(data=request.POST)
        if comment_form.is_valid():
            new_element = comment_form.save(commit=False)
            new_element.post = post
            new_element.save()
            return redirect("app:chart", slug) # redirect to this url
    else:
        comment_form = ElementForm()
    context= {
        'elements': elements,
        'comment_form': comment_form,
        "chart":chart,
        "elements_count":elements_count,
        "number_avg":number_avg,
        }
    
    return render(request, "pages/chart.html", context)

def ProfileView(request, username):
        user_p = User.objects.get(username=username)
        author = get_object_or_404(User, username=username)
        return render(request, 'pages/profile.html')

def NewChartView(request):
    user_p = User.objects.get(username=request.user)
    user = User.objects.get(username=request.user)
    author = get_object_or_404(User, username=request.user)
    dash = author.chart.all()
    new_dash = None
    NewChart = ChartFrom()
    if request.method == 'POST':
        NewChart = ChartFrom(data=request.POST)
        if NewChart.is_valid():
            new_dash = NewChart.save(commit=False)
            new_dash.author = author
            new_dash.save()
            slug = NewChart.cleaned_data.get('slug')
            return redirect("app:chart", slug) 
   
    context={
        "NewChart":NewChart,
    }
    return render(request, "pages/new.html", context)