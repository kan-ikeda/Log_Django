from django.urls import path
from . import views

app_name = 'mylog'
urlpatterns = [
    path('',views.LogListView.as_view(), name='log_list'), #ホーム（日記一覧）
    path('log/add/', views.LogCreateView.as_view(), name='log_create'), #日記作成
    path('log/<int:pk>/', views.LogDetailView.as_view(), name='log_detail'), # 日記詳細
    
]