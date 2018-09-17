monster    = ['タコケン・レイダー', 'ストームトルッパ', 'ジャンゴン']
attack     = ['ライトセーバー', 'ターボレーザー', 'ブラスターライフル']
fight_back = ['反撃', '防御', '逃走']

# リストの要素の数だけ繰り返す
for mst, atc, fb in zip(monster, attack, fight_back):
    print(mst + 'があらわれた！\n',                        # モンスターの出現
          '>>>勇者は{}をふりかざした!'.format(atc) + '\n', # 勇者の反応
          '>>>{}が{}した！'.format(mst, fb)                # モンスターの反応
          )
