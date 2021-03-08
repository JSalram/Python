from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import *


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
    template_name = 'comment_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = get_object_or_404(Article, pk=self.kwargs['fk'])
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
