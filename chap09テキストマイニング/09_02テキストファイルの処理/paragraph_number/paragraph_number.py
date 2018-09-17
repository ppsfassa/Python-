file = open('kusamakura.txt') # ファイルをオープン
counter = 0
for line in file:             # センテンス単位で取り出す
  counter += 1
  line = line.strip()         # 前後の空白と末尾の改行を取り除く
  print(str(
    counter) + ' : ' + line)  # 番号を付けて段落を出力
file.close()                  # Fileオブジェクトを閉じる
