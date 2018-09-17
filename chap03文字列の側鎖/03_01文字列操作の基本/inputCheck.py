while True:
    age = input('年齢を入力してください：')
    if age.isdecimal():    # 数字であるかをチェック
        break
    print('年齢は数字であることが必要です')

while True:
    password = input('パスワードを入力してください(英数字のみ)：')
    if password.isalnum(): # 英数字であるかをチェック
        break
    print('パスワードは英数字であることが必要です')
