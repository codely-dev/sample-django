from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Location

class LocationList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Location
    context_object_name = 'all_locations'

    def get_context_data(self, **kwargs):
        context = super(LocationList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

class LocationView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Location
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context