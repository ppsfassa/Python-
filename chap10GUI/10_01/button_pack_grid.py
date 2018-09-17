import tkinter as tk

root = tk.Tk()                                   # メインウィンドウを作成
root.geometry('100x100')                         # ウィンドウのサイズを設定
button1 = tk.Button(
    root, text='ボタン1').grid(row=0, column=0)  # 1行目の1列目にボタンを配置

button2 = tk.Button(
    root, text='ボタン2').grid(row=0, column=1)  # 1行目の2列目にボタンを左に配置

button3 = tk.Button(
    root, text='ボタン3').grid(row=1, column=1)  # 2行目の2列目にボタンを右に配置

root.mainloop()
