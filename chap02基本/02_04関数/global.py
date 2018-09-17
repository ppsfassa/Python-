def msg():
    global word    # グローバル変数を変更できるようにする
    word = 'Hello' # グローバル変数の値を設定

word = 'global'    # グローバル変数
msg()              # msg()を呼出す
print(word)        # グローバル変数の値を出力
