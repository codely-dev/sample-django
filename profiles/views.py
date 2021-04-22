from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Profile

@login_required(login_url=reverse_lazy('login'))
def detail(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})