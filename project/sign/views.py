from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm
from callboard.models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from callboard.utils import menu


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = reverse_lazy('user_view')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class BaseLoginView(LoginView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


class BaseLogoutView(LogoutView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context

