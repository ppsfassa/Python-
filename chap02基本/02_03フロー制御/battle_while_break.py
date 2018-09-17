print('まものたちがあらわれた！')    # 最初に出力
brave = input('お名前をどうぞ！>')   # プレイヤーの名前を取得
prompt = brave + 'の呪文 > '         # プロンプトを作る
attack = ''                          # 呪文を代入する変数を用意
counter = 0


while counter < 3:                   # attackが'ジェダイ'でない限り繰り返す
    attack = input('' + prompt)      # 呪文を取得
    print(brave + 'は「' + attack + '」の呪文をとなえた！')

    if attack == 'ジェダイ':         # attackが'ジェダイ'なら終了
        print('まものたちは全滅した')
        break                        #ここでwhileループを抜ける
    else:
        print('まものたちはようすをうかがっている')

    counter = counter + 1            # 1を加算

if counter == 3:                     # 3回繰り返した場合の処理
    print('まものたちはどこかへ行ってしまった...')
