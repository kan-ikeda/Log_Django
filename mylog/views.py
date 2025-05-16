from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Log
from .form import LogForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile



# Create your views here.

#日記一覧（ホーム）
class LogListView(ListView):
    model = Log
    template_name = 'mylog/log_list.html'
    context_object_name = 'logs'


# マイページ
class MyPageView(LoginRequiredMixin, ListView):
    model = Log
    template_name = 'mylog/mypage.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return Log.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile  # profile を追加
        return context

# 日記作成
class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    form_class = LogForm
    template_name = 'mylog/log_create.html'
    success_url = reverse_lazy('mylog:log_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# 日記詳細
class LogDetailView(DetailView):
    model = Log
    template_name = 'mylog/log_detail.html'
    context_object_name = 'log'
