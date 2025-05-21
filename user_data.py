# users_data.py
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

users_data = [
    {
        'username': 'testuser',
        'password': 'testpassword',  # 安全なパスワードに変更してください
        'email': 'test@example.com',
        'is_staff': False,
        'is_superuser': False,
    },
]

for user_data in users_data:
    # パスワードをハッシュ化
    hashed_password = make_password(user_data['password'])
    
    User.objects.create(
        username=user_data['username'],
        password=hashed_password,
        email=user_data['email'],
        is_staff=user_data['is_staff'],
        is_superuser=user_data['is_superuser'],
    )

print('ユーザー初期データの投入が完了しました。')