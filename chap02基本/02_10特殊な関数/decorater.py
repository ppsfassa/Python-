def hello():
    return "ごぶさた！"

# 関数を受け取り関数を返す高階関数
def dec(func):
    def new_func():
        print ('function called:' + func.__name__)
        return func()
    return new_func

# hello()関数を書き換え
hello = dec(hello)

print (hello())
