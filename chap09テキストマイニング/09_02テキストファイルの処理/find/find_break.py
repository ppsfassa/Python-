file = open('sample.txt')     # ファイルをオープン
for line in file:             # センテンス単位で取り出す
  line = line.rstrip()        # 行末尾の改行を取り除く
  if 'オブジェクト' in line:  # センテンスの中に指定した文字列が含まれるか
    print('見つかりました!')
    print(line)               # 文字列を含センテンスを出力
    break                     # ループを抜ける
file.close()                  # Fileオブジェクトを閉じる
