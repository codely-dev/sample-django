from django.db import models
from django.contrib.auth.models import User
from locations.models import Location
from django.db.models.constraints import UniqueConstraint

class Event(models.Model):
    title = models.CharField(max_length=32)
    startdate = models.DateTimeField('Start')
    enddate = models.DateTimeField('Ende')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    description = models.TextField('Beschreibung', blank=True)
    submitted = models.DateField('Erstelldatum', auto_now_add=True)
    category = models.IntegerField('Icon', choices=[
        (1, 'Höhenflug'), 
        (2, 'Übungshang'), 
        (3, 'Theorie'),  
        (4, 'Reisen'),
        (5, 'SIKU/NSW'),
        (6, 'Sonstiges'),
        ]
    )
    participants = models.ManyToManyField(User, blank=True, related_name='Teilnehmer')
    organisator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='Organisator')

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField('Kommentar', blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    submitted = models.DateTimeField('Erstelldatum', auto_now_add=True)

    def __str__(self):
        return str(self.id)