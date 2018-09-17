import tkinter as tk

root = tk.Tk()                                # メインウィンドウを作成
root.geometry('200x200')                      # ウィンドウのサイズを設定

button1 = tk.Button(
    root, text='ボタン1').place(x=0, y=0)     # ウィンドウの左上隅に配置

button2 = tk.Button(                          # 左端から50px、
    root, text='ボタン2').place(x=50, y=50)   # 上端から50pxの位置に配置

button3 = tk.Button(                          # 左端から100px、
    root, text='ボタン3').place(x=100, y=100) # 上端から100pxの位置に配置

root.mainloop()
