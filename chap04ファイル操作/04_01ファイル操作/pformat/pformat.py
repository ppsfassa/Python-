import pprint                  # pprintのインポート

# 辞書のリストを作成
name_id = [{'name':'秀和太郎', 'id':'A101'},
           {'name':'秀和花子', 'id':'B101'},
           {'name':'築地次郎', 'id':'A102'}]

# ソースファイルを書き込みモードで開く
file = open('customer.py',     # ファイル名
            'w',               # 書き込みモードを指定
            encoding = 'utf-8' # 文字コードをUTF-8にする
            )
# リストの定義コードを作成してファイルに書き込む
file.write('name_id = ' + pprint.pformat(name_id) + '\n')
# ファイルを閉じる
file.close()

