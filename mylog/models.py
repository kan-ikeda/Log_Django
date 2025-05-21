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

    def __str__(self):
        return self.title
