def show_wordlist(file):
    word_lst = []                       # 単語リストを用意
    file_data = open(file)              # ファイルをオープン
    for line in file_data:              # 段落を取り出す
      tmp_lst = line.split()            # 単語に分割してリストにする(改行は除かれる)

      for word in tmp_lst:              # リストから単語を取り出す
        word = word.rstrip('.,:!?)’”')# 末尾のピリオド等を取り除く
        word = word.lstrip('(‘“')     # 冒頭のクォートを取り除く
        word_lst.append(word)           # 単語リストに追加する

    return word_lst

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    file_name = input('ファイル名を入力してください>>>')
    lst = show_wordlist(file_name)     # 読み込むファイルを指定して単語リストを取得
    for word in lst:                   # 単語リストから単語を取り出す
      print(word)                      # 出力
