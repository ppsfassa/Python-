def square():
    global word       # グローバル変数を変更できるようにする
    word = 'square'   # グローバル変数に代入する

def triangle():
    word = 'triangle' # ローカル変数word

def show():
    print(word)       # グローバル変数を参照する

word = 'form'         # グローバル変数
square()              # square()を実行
show()                # show()を実行
print(word)           # グローバル変数wordを出力
