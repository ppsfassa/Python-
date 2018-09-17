def sequence (*args):
    for s in(args):     # 渡された引数の数だけ繰り返す
        print(s + '月') # タプルから取り出した値を表示

sequence('1','2','3')   # 必要なだけ引数を指定して関数を呼び出す
