# 初期データ投入用のスクリプト tags_data.py
from mylog.models import Tag


# タグの作成
tags = ['日常','旅行','景色','グルメ','仕事','癒し','趣味','健康','趣味']

for tag_name in tags:
    Tag.objects.create(name=tag_name)

print('初期データの投入が完了しました。')