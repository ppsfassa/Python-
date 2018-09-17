def get_frequency(file):
    freq = {}                           # 辞書を用意

    file_data = open(file)              # ファイルをオープン
    for line in file_data:              # 段落を取り出す
      words = line.split()              # 単語に分割してリストにする(改行は除かれる)

      for word in words:                # リストから単語を取り出す
        word = word.rstrip('.,:!?)’”')# 末尾のピリオド等を取り除く
        word = word.lstrip('(‘“')     # 冒頭のクォートを取り除く
        
        if word in freq:                # 辞書に単語と同じキーがあるか
          freq[word] += 1               # キーの値に1加算
        else:                           # 該当するキーがなければ
          freq[word] = 1                # 単語をキーにして値を1にする
          
    return freq                         # 頻度表としての辞書を返す

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    file_name = input('ファイル名を入力してください>>>')
    freq = get_frequency(file_name)          # ファイルを指定して頻度表の辞書を取得
    
    for word in freq:                        # 辞書のキー(単語)を取り出す
      print(
          word + '(' + str(freq[word]) + ')' # キー(単語)と値(頻度)を出力
          )

