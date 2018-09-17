# 2つのパラメーターを持つ関数
def appear(name,                         # パラメーター名のみ
           action = '逃げだした'         # パラメーターのデフォルト値を設定
           ): 
    result = name + 'が' + action + '！'
    return result                        # 処理した文字列を戻り値として返す

show = appear('シスの暗黒卿')            # nameに渡す
print(show)                              # 関数の戻り値を出力
