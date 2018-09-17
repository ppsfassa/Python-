file = open('sample_blank.txt')
for line in file:
  line = line.rstrip()
  if not line == '':      # 空白行ではない場合に出力
      print(line)
file.close()              # Fileオブジェクトを閉じる

file = open('sample_blank.txt')
for line in file:
  line = line.rstrip()
  if line == '': # 空白行の場合
    continue     # スキップして次の繰り返しに進む
  print(line)    # 空白ではないセンテンスだけを出力
file.close()     # Fileオブジェクトを閉じる
