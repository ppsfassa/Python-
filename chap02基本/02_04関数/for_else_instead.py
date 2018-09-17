def test(x, y):
    for i in range(2,                 # 2から始める
             min(x, y) + 1            # 2つの数の小さいほうの数まで繰り返す
             ):
        print('%d で試します' % i)
        if x % i == 0 and y % i == 0: # 公約数があればFalseを返す
            return False
    return True                       # 1以外に公約数がなければTrueを返す

x = 4
y = 9

if(test(x, y)):                       # 1以外に公約数がない場合
   print('2つの数は互いに素です')
else:                                 # 1以外に公約数がある場合
   print('2つの数は互いに素ではありません')
