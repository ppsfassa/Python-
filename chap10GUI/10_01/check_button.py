import tkinter as tk

# チェックボタンに表示する文字列を用意
item  = ['腕時計','手帳', '預金通帳', '傘']
# BooleanVarオブジェクトを格納するためのリスト
check = {}

root = tk.Tk()                  # メインウィンドウを作成
root.geometry('200x150')        # ウィンドウのサイズを設定

# チェックボタンの作成と配置
# itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
    # BooleanVarオブジェクトを作成してリストcheckの要素にする
    check[i] = tk.BooleanVar()
    # チェックボタンの作成と配置
    tk.Checkbutton(root,                # 親要素を指定
                   variable = check[i], # variableにリストcheckのi番目の要素を指定
                   text = item[i]       # textにリストitemのi番目の要素を指定
                   ).pack(anchor=tk.W)  # 左寄せで配置する

# チェックボタンの状態を通知する関数
def choice():
    # リストcheckの要素の数だけ繰り返す
    for i in check:
        # checkのi番目のBooleanVarオブジェクトのTrue／Falseを調べる
        if check[i].get() == True:
            print(item[i] + 'をお忘れなく')

# ボタンの作成と配置
button = tk.Button(root,
                   text = '明日の持ちもの',
                   command = choice     # クリック字にchoice()関数を呼ぶ
                   ).pack()

root.mainloop()
