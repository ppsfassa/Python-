import os

# カレントディレクトリのファイル名を取得
for filename in os.listdir():
    # 拡張子が.txtの場合の処理
    if filename.endswith('.txt'):
        print(filename)                  # ファイル名出力
        ans = input('削除しますか？(Y)') # 削除するか確認

        if ans == 'Y':                   # 'Y'が入力されたら
            os.unlink(filename)          # 完全に削除する


