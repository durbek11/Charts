from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.db.models import Avg
from django.views import generic
from django.urls import reverse 
from django.db.models import Q
from .models import *
from .forms import *
User = get_user_model()


def home(request):
    charts_count = Chart.objects.count()
    user_count = User.objects.count()
    date_joined_count = User.objects.filter(date_joined__date=timezone.now()-timezone.timedelta(0)).count()
    users = User.objects.all().order_by('-id')[:date_joined_count]
    elem_count = Element.objects.count()
    following_actions = None
    # created_on_count = None
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        # for user_f in user.followers.all():
        #     created_on_count = user_f.chart.filter(created_on__date=timezone.now()).count()
        following_actions = user.followers.all().order_by('-id')[:15]

    contact = ContactUsForm()
    if request.method == "POST":
        contact = ContactUsForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('app:home')
    context = {
        "charts_count":charts_count,
        "user_count":user_count,
        "elem_count":elem_count,
        "following_actions":following_actions,
        "users":users,
        "contact":contact
    }
    return render(request, 'pages/home.html', context)

