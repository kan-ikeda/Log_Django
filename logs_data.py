from datetime import date
from django.contrib.auth.models import User
from mylog.models import Log,Tag


try:
    testuser = User.objects.get(username='CapyCapy')
except User.DoesNotExist:
    # testuser が存在しない場合はエラーを表示して終了
    print("Error: testuser does not exist. Please create it first.")
    exit()

try:
    testuser_wallaby = User.objects.get(username='Wallaby')
except User.DoesNotExist:
    # ユーザーが存在しない場合はエラーを表示して終了
    print("Error: User 'Wallaby' does not exist. Please create it first.")
    exit()


logs_data = [
    {
        'title': '初めての日記',
        'date': date(2024, 1, 1),
        'author': 'CapyCapy', 
        'content': '今日から日記を始めます。',
        'tags': ['旅行'],  # タグ名を指定
        'image':'logs/data_image3.jpg',
    },
    {
        'title': '旅行の思い出',
        'date': date(2023, 12, 25),
        'author': 'Wallaby',  # ユーザーオブジェクトを直接指定
        'content': 'きれいな景色だね～',
        'tags': ['旅行'],  # タグ名を指定
        'image':'logs/data_image1.jpg',
    },
    {
        'title': '今日のランチ',
        'date': date(2024, 1, 2),
        'author': 'CapyCapy',  # ユーザー名を指定
        'content': '美味しいラーメンを食べました。',
        'tags': ['グルメ'],  # タグ名を指定
        'image':'logs/data_image2.jpg',
    },
    {
        'title': '初めての京都旅行',
        'date': date(2025, 4, 20),
        'author': 'CapyCapy',
        'content': '京都に行ってきました！清水寺は圧巻。抹茶スイーツも堪能しました。',
        'tags': ['旅行'],
        'image': 'logs/data_image4.jpg',
    },
    {
        'title': '沖縄の海',
        'date': date(2024, 8, 17),
        'author': 'Wallaby',
        'content': '沖縄の海は本当に綺麗だった。シュノーケリングで熱帯魚も見れた！',
        'tags': ['旅行'],
        'image': 'logs/data_image5.jpg', 
    },
]

for log_data in logs_data:
    # ユーザーを取得
    try:
        user = User.objects.get(username=log_data['author'])
    except User.DoesNotExist:
        print(f"Error: User '{log_data['author']}' does not exist.")
        continue


    # タグを取得
    tags = []
    for tag_name in log_data['tags']:
        try:
            tag = Tag.objects.get(name=tag_name)
            tags.append(tag)
        except Tag.DoesNotExist:
            print(f"Error: Tag '{tag_name}' does not exist.")
            continue  # 次のタグへ


    log = Log.objects.create(
        title=log_data['title'],
        date=log_data['date'],
        author=user,
        content=log_data['content'],
        image=log_data['image'],
    )

    
    # タグを追加
    log.tags.set(tags)



print('初期データの投入が完了しました。')