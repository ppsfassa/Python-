print('まものたちがあらわれた！')    # 最初に出力
brave = input('お名前をどうぞ！>')   # プレイヤーの名前を取得
prompt = brave + 'の呪文 > '         # プロンプトを作る
attack = ''                          # 呪文を代入する変数を用意

while attack != 'ジェダイ':          # attackが'ジェダイ'でない限り繰り返す
    attack = input('' + prompt)      # 呪文を取得
    print(brave + 'は「' + attack + '」の呪文をとなえた！')

    if attack != 'ジェダイ':         # attackが'ジェダイ'でなければ以下を表示
        print('まものたちは様子をうかがっている')

print('まものたちは全滅した')
