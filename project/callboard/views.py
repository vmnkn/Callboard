from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from .filters import PostFilter
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import menu


class PostList(ListView):
    model = Post
    template_name = 'callboard/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filterset'] = self.filterset
        context['comments'] = Comment.objects.all()
        context['menu'] = menu
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostDetail(DetailView):
    model = Post
    template_name = 'callboard/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'callboard/post_create.html'
    success_url = reverse_lazy('post_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'callboard/post_update.html'
    success_url = reverse_lazy('post_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'callboard/post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'callboard/account.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class CommentCreate(LoginRequiredMixin, TemplateView):
    form_class = CommentForm
    model = Comment
    template_name = 'callboard/comment_create.html'
    success_url = reverse_lazy('post_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class CommentDelete(LoginRequiredMixin, TemplateView):
    model = Comment
    template_name = 'callboard/comment_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context