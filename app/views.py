from typing import Any
from django import http
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm
from datetime import date
from django.shortcuts import redirect

class AgeRestrictionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.birth_date:
            today = date.today()
            age = today.year - request.user.birth_date.year - ((today.month, today.day) < (request.user.birth_date.month, request.user.birth_date.day))
            if age < 21:
                return redirect('underage_page') 
        return super().dispatch(request, *args, **kwargs)

class Dashboard(LoginRequiredMixin, AgeRestrictionMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = reverse_lazy('login')

class UnderAge(LoginRequiredMixin, TemplateView):
    template_name = 'underage_page.html'
    login_url = reverse_lazy('login')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('dashboard')

class Logout(LogoutView):
    next_page = reverse_lazy('login')