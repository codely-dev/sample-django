from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitted','url')
    readonly_fields = ('submitted',)
    ordering = ['submitted']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)