import tkinter as tk

def push():
    print('押しましたね')

root = tk.Tk()                  # メインウィンドウを作成
root.geometry('100x50')         # ウィンドウのサイズを設定
button = tk.Button(root,
                   text='押してね',
                   command=push
                   ).pack()

root.mainloop()
