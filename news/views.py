from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article

class ArticleList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Article
    context_object_name = 'all_articles'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['news_list'] = Page.objects.all()
        return context