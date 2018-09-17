import traceback

def func1(): # func2()を呼出す関数
    func2()

def func2(): # 例外を発生させる関数
    raise Exception('func1()のエラーメッセージです。')

try:
    func1()      # func1()を呼出す
except:
    err_file = open('error.txt', 'w')
    err_file.write(traceback.format_exc())
    err_file.close()
    print('トレースバックをerror.txtに記録しました。')
