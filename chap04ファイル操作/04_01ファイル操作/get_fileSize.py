import os

size = 0                       # ファイルサイズを保持する変数
path = 'C:\\Windows\\System32' # フォルダーのパス

# フォルダー内のすべてのファイル名をループ処理
for filename in os.listdir(path):
    # ファイルサイズを取得してsizeに足し合わせる
    size = size + os.path.getsize(
                     # ディレクトリパスとファイル名を連結してフルパスを作る
                     os.path.join(path, filename)
                     )
# 合計サイズを出力
print(size)
