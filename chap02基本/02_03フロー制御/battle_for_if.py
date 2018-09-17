name    = input('お名前をどうぞ>')	# プレイヤーの名前を取得
brave   =  (name + 'の攻撃！')          # プレイヤーの攻撃パターン
mamono1 = 'まものたちはひるんでいる'	# 魔物の応答パターン1
mamono2 = 'まものたちはたいさんした'	# 魔物の応答パターン2

# 名前が入力されたらバトル開始
if (brave):
    print('まものたちがあらわれた！')
    # 10回繰り返す
    for count in range(10):
        # 偶数回の処理ならプレイヤーの攻撃を出力
        if count % 2 ==0:
            print(brave)
        # 奇数回の処理なら魔物たちの応答mamono1を出力
        else:
            print(mamono1)
    # for文終了後に魔物たちの応答mamono2を出力
    print(mamono2)
# 何も入力されなければゲームを終了
else:
    print('ゲーム終了')
