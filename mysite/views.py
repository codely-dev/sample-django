from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_list_or_404

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from events.models import Event
from news.models import Article

def homepage(request):
    return render(request, 'homepage.html')

@login_required(login_url=reverse_lazy('login'))
def dashboard(request):
    if request.method == 'GET':
        events = get_list_or_404(Event)
        articles = get_list_or_404(Article)
        context = {
            'events': events,
            'articles': articles,
        }
        return render(request, 'dashboard.html', context)
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
        return HttpResponseRedirect('/dashboard')



from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)