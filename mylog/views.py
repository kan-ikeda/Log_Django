from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView, View
from .models import Log, Comment, Like
from .form import LogForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile
from django.http import HttpResponseRedirect



# Create your views here.

#日記一覧（ホーム）
class LogListView(ListView):
    model = Log
    template_name = 'mylog/log_list.html'
    context_object_name = 'logs'
    ordering = ['-datetime']

    def get_queryset(self):
        return Log.objects.filter(is_public=True).order_by('-datetime') 


# マイページ
class MyPageView(LoginRequiredMixin, ListView):
    model = Log
    template_name = 'mylog/mypage.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return Log.objects.filter(author=self.request.user).order_by('-datetime')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log = self.get_object()
        context['comments'] = log.comments.order_by('-created_at')  # コメントを新しい順に取得
        context['comment_form'] = CommentForm()  # コメントフォーム
        context['like_count'] = log.likes.count()  # いいねの数を取得
        return context


# 日記削除
class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = Log
    template_name = 'mylog/delete_confirm.html'
    success_url = reverse_lazy('mylog:mypage')  # 削除後にマイページへリダイレクト
    context_object_name = 'log'

    def get_queryset(self):
        return Log.objects.filter(author=self.request.user)  # 自身の投稿のみ削除可能


# コメント投稿
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'mylog/add_comment.html'  # 必要に応じてテンプレートを作成
    # 投稿完了後、詳細ページへリダイレクト
    def get_success_url(self):
        return reverse_lazy('mylog:log_detail', kwargs={'pk': self.kwargs['log_id']})

    def form_valid(self, form):
        log_pk = self.kwargs['log_id']
        log = get_object_or_404(Log, pk=log_pk)
        comment = form.save(commit=False)
        comment.log = log
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

#いいね機能
class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        log = get_object_or_404(Log, pk=pk)
        like, created = Like.objects.get_or_create(log=log, user=request.user)
        if not created:
            like.delete()
        return HttpResponseRedirect(reverse('mylog:log_detail', args=[pk]))