  
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Event, Comment
from .forms import EventForm, ParticipationForm, CommentForm
from django.contrib.auth.models import User

@login_required(login_url=reverse_lazy('login'))
def list(request):
    if request.method == 'GET':
        events = get_list_or_404(Event)
        context = {
            'events': events,
        }
        return render(request, 'events/event_list.html', context)
    if request.method == 'POST':
        form = request.POST
        #GET Form Values
        event_id = form.get("event")
        participate = form.get("participate")
        event = Event.objects.get(id=event_id)
        #Event Anmeldung
        if participate == "1":
            event.participants.add(request.user)
        #Event Abmeldung
        if participate == "0":
            event.participants.remove(request.user)
        return HttpResponseRedirect('/events')

@login_required(login_url=reverse_lazy('login'))
def detail(request, pk):
    event = get_object_or_404(Event, id=pk)
    comments = get_list_or_404(Comment, event__pk=pk)
    #POST-Request
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #Add Comment to Database
            Comment(event=event, content=cd.get("comment"), username=request.user).save()
            return HttpResponseRedirect('?submitted')
    #GET-Request
    else:
        form = CommentForm()
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'form': form,})