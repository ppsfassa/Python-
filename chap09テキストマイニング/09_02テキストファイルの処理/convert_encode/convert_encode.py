def convert_encode(file, encord):
    file_input = open(file + '.txt',        # ファイルをオープン
                      'r',                  # 読み取り専用で開く
                      encoding = encord     # パラメーターで取得したエンコード方式
                      )
    
    file_output = open(file + '_utf-8.txt', # ファイルをオープン(新規作成)
                      'w',                  # 書き換えモード
                      encoding = 'utf-8'    # utf-8で保存する
                      )
    
    for line in file_input:                 # 改行までを1つの段落として取り出す
      print(line,                           # 段落を書き込む
            file = file_output,             # 出力先をfile_outpuにする
            end  = ''                       # print()独自の改行は出力しない
            )

    file_input.close()                      # Fileオブジェクトをクローズ
    file_input.close()                      # Fileオブジェクトをクローズ

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    file_name = input('ファイル名を入力してください>>>')
    encoding  = input('ファイルのエンコード方式を入力してください>>>')
    # 指定したファイルをUTF-8に変換して別名のファイルに保存する
    convert_encode(file_name, encoding)
