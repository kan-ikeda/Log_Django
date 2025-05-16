from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Log

# 基本的な登録方法
admin.site.register(Log)
