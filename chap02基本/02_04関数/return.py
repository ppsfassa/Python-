def appear(word1, word2):                   # 2つのパラメーターを持つ関数
    result = word1 + 'と' + word2 + 'があらわれた！'
    return result                           # 処理した文字列を戻り値として返す

show = appear('ベイダー卿', 'シスの暗黒卿') # 引数を2つ設定して関数を呼び出す
print(show)                                 # 関数の戻り値を出力
