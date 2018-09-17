while True:
    name = input('お名前をどうぞ！>')   # 名前を取得
    if name != 'アナキン':              # 入力された名前をチェック
        print('そんな人は知りません!')
        continue                        # 名前が一致しなければループの先頭に戻る
    password = input(
        'ようこそ!パスワードをどうぞ>') # 名前が一致したらパスワードを尋ねる
    if password == 'good':              # パスワードのチェック
        break                           # パスワードが一致したらループを抜ける
print('認証しました')

                    
