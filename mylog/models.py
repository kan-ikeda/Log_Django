from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#タグモデル
class Tag(models.Model):
    name = models.CharField('タグ', max_length=100)

    def __str__(self):
        return self.name


#日記モデル
class Log(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('画像', upload_to='logs/', blank=True, null=True)
    date = models.DateField('日付', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    content = models.TextField('内容', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='タグ')
    datetime = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def truncated_title9(self, length=9):
        if len(self.title) > length:
            return self.title[:length] + "…"
        return self.title
    
    def truncated_title11(self, length=11):
        if len(self.title) > length:
            return self.title[:length] + "…"
        return self.title

    def __str__(self):
        return self.title

# コメントモデル
class Comment(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, verbose_name='日記', related_name='comments')  # 紐付ける日記
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='投稿者')  # コメントしたユーザー
    content = models.TextField('コメント内容')
    created_at = models.DateTimeField('投稿日時', auto_now_add=True)

    def __str__(self):
        return self.content[:20]  

# いいねモデル
class Like(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, verbose_name='日記', related_name='likes')  # 紐付ける日記
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')  # いいねしたユーザー
    created_at = models.DateTimeField('いいね日時', auto_now_add=True)

    class Meta:
        # ユーザーが同じ投稿に複数回いいねできないようにする
        unique_together = ('log', 'user')