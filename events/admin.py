from django.contrib import admin
from .models import Event, Comment#, Participation

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'startdate', 'enddate', 'location')
    readonly_fields = ('submitted',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'submitted', 'username')
    readonly_fields = ('submitted',)

admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
