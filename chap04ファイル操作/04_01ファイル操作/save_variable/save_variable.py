import shelve

# データ登録1回目
shelve_file = shelve.open('friend')              # ファイルオープン
my_friend = ['秀和太郎', '秀和花子', '築地次郎'] # 保存データを作成 
shelve_file['my_friend'] = my_friend             # データを保存する
shelve_file.close()                              # ファイルを閉じる
print('ファイルを保存しました。')


# データの読み込みのみ
print('ファイルをオープンします。')
shelve_file = shelve.open('friend')              # friendファイルを開く
print(shelve_file['my_friend'])                  # 保存済みのデータを取得
print('ファイルをクローズします。')
shelve_file.close()                              # ファイルを閉じる

# データ登録2回目
shelve_file = shelve.open('friend')              # friendファイルを開く
id = ['A1', 'B2', 'A2']                          # 保存データを作成 
shelve_file['id'] = id                           # データを保存する

keys = list(shelve_file.keys())                  # 登録済みのキーの一覧を取得
print('keys = ', keys)
values = list(shelve_file.values())              # 登録済みの値の一覧を取得
print('values = ', values)
