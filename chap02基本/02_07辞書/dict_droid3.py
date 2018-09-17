droid= {'R2-D2'            : '宇宙用のアストロメク・ドロイド',
        'C-3PO'            : '知覚生物とコミュニケーションを取るためのドロイド',
        'バトル・ドロイド' : '戦闘用に設計されたドロイド'
        }
val = droid.values()       # 辞書の値のみをすべて取り出す
print(val)

for key in droid.values(): # values()の戻り値をforでイテレートする
    print(key)
