def func1(): # func2()を呼出す関数
    func2()

def func2(): # 例外を発生させる関数
    raise Exception('func1()のエラーメッセージです。')

func1()      # func1()を呼出す

