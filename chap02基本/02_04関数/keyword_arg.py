def appear(name, action):                # 2つのパラメーターを持つ関数
    result = name + 'が' + action + '！'
    return result                        # 処理した文字列を戻り値として返す

show = appear(action = 'あらわれた',     # actionに渡す
              name = 'ベイダー卿'        # nameに渡す
              )
print(show)                              # 関数の戻り値を出力

show = appear('ベイダー卿',              # nameに渡す
              action = 'あらわれた',     # actionに渡す
              )
print(show)                              # 関数の戻り値を出力
