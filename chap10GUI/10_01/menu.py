import tkinter as tk
import tkinter.messagebox

# ［閉じる］アイテムが選択されたときに呼ばれる関数
def callback():
    # メッセージボックスの[はい]ボタンクリック時の処理
    if tk.messagebox.askyesno(
        'Quit?', '終了する？'):
        root.destroy()
    # [いいえ]ボタンクリックしたら何もしない

# メインウィンドウを作成
root = tk.Tk()                  

# [閉じる]ボタンがクリックされたらcallback()関数を呼ぶ
root.protocol('WM_DELETE_WINDOW', callback)

# メニューバーのためのMenuオブジェクトを作成
menubar = tk.Menu(root)
# ウィンドウのメニューバーとして登録
root.config(menu=menubar)
# メニューのためのMenuオブジェクトを生成
# 引数はメニューバー
filemenu = tk.Menu(menubar)
# ［ファイル］メニューをメニューバーに配置
menubar.add_cascade(label='ファイル', menu=filemenu)
# ［閉じる］アイテムを配置
filemenu.add_command(label='閉じる', command=callback)

root.mainloop()
