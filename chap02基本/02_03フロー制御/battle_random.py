import random                          # randomモジュールのインポート

print('まものたちがあらわれた！')      # 最初に出力

brave   = input('お名前をどうぞ！>')   # 勇者の名前を取得
brave1  = brave + 'のこうげき！'       # 1つ目の攻撃パターンを作る
brave2  = brave + 'は呪文をとなえた！' # 2つ目の攻撃パターン
mamono1 = 'まものたちはひるんでいる'   # 魔物の反応その1
mamono2 = 'まものたちがはんげきした！' # 魔物の反応その2

if(brave):
    print(brave1)                      # 繰り返しの前に勇者の攻撃を出力しておく
    for count in range(10):            # 繰り返す回数は10回
        x = random.randint(1, 10)      # 1～10の範囲の値をランダムに生成
        if x <= 3:                     # 生成された値が3以下であればbrave1
            print(brave1)
        elif 4 <= x <= 6:              # 生成された値4以上6以下であればbrave2
            print(brave2)
        elif 7 <= x <= 9:              # 生成された値が7以上9以下であればmamono1
            print(mamono1)
        else:                          # 生成された値が上記以外はmamono2
            print(mamono2)
    print('まものたちはたいさんした')
else:
    print('ゲーム終了')                # 名前が入力されなかった場合は何もせずに終了

