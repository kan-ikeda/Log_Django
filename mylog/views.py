from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Log
from .form import LogForm
from django.urls import reverse_lazy


# Create your views here.

#日記一覧（ホーム）
class LogListView(ListView):
    model = Log
    template_name = 'mylog/log_list.html'
    context_object_name = 'logs'

# 日記作成
class LogCreateView(CreateView):
    model = Log
    form_class = LogForm
    template_name = 'mylog/log_create.html'
    success_url = reverse_lazy('mylog:log_list')

# 日記詳細
class LogDetailView(DetailView):
    model = Log
    template_name = 'mylog/log_detail.html'
    context_object_name = 'log'
    