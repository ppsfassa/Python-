import tkinter as tk

# ラジオボタンに表示する文字列を用意
item = ['庭の掃除', '窓ふき', '車の洗車', '床のワックスがけ']

root = tk.Tk()                         # メインウィンドウを作成
root.geometry('200x150')               # ウィンドウのサイズを設定
val = tk.IntVar()                      # IntVarオブジェクトを作成して変数に代入

# ラジオボタンの作成と配置
# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    tk.Radiobutton(root,# 親要素を指定
                   value = i,          # valueの値をiにする
                   variable =val,      # variableにIntVarオブジェクトを指定
                   text = item[i]      # textにリストitemのi番目の要素を指定
                   ).pack(anchor=tk.W) # 左寄せで配置する

# ラジオボタンの状態を通知する関数
def choice():
    ch = val.get()                     # IntVarオブジェクトの値を取得
    # リストitemのインデックスをchに指定して要素を出力
    print('明日は' + item[ch] + 'をやりましょう')

# ボタンの作成と配置
button = tk.Button(root,
                   text = '明日やること',
                   command = choice    # クリック時にchoice()関数を呼ぶ
                   ).pack()

root.mainloop()
