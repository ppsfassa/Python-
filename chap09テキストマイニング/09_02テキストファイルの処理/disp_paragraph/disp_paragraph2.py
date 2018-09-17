def paragraph(file, num):
  file_data = open(file)        # ファイルをオープン
  counter = 0                   # カウンター変数を初期化
  for line in file_data:        # 段落単位で取り出す
    line = line.rstrip()        # 末尾の改行のみを取り除く
    counter += 1                # カウンター変数の値を1増やす
    if counter==num:            # 指定した段落数に達したらループを抜ける
      print(line)               # ①段落を出力
      break
  file_data.close()             # Fileオブジェクトを閉じる

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
  f_name = input('ファイル名を入力してください>>>')
  p_num  = int(input('読み出す段落の数を入力してください>>>'))
  paragraph(f_name, p_num)  # ファイル名と段落数を指定してparagraph()を実行
