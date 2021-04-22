from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Event
        fields = [
            'title',
            'startdate',
            'enddate',
            'location',
            'description',
        ]

class ParticipationForm(forms.Form):
    value = forms.CharField(widget = forms.HiddenInput())
    event = forms.IntegerField(widget = forms.HiddenInput())

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':50}), label=False)