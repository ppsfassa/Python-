import os, shutil

# 削除するフォルダーのパスを取得
path = input('削除するフォルダーのパスを入力してください>')

if os.path.isdir(path):              # 指定されたパスが存在する
    print(path)                      # 指定されたパスを出力
    ans = input('削除しますか？(Y)') # 削除するか確認
    if ans == 'Y':                   # 'Y'が入力されたら
        shutil.rmtree(path)          # 完全に削除する

else:                                # 指定されたパスが存在しない
    print('指定したフォルダーは存在しません。')
        

