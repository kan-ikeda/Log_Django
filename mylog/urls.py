from django.urls import path
from . import views

app_name = 'mylog'
urlpatterns = [
    path('',views.LogListView.as_view(), name='log_list'), #ホーム（日記一覧）
    path('create/', views.LogCreateView.as_view(), name='log_create'), #日記作成
    path('<int:pk>/', views.LogDetailView.as_view(), name='log_detail'), # 日記詳細
    path('mypage/', views.MyPageView.as_view(),name= 'mypage'), #マイページ
    path('delete/<int:pk>', views.LogDeleteView.as_view(), name='delete_log'),#日記削除
    path('comment/<int:log_id>/', views.AddCommentView.as_view(), name='add_comment'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like'),
]