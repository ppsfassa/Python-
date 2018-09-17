import tkinter as tk                    # tkinterのインポート
import random                           # randomのインポート

#グローバル変数の定義
response_area = None # 応答エリアのオブジェクトを保持

# 明日の予定を決める関数
def wakuwaku():
    play =  ['小っちゃな映画館を探して映画を観に行く',
             'おしゃれなカフェでまったりする',
             '絶叫マシンの遊園地ではしゃぐ',
             'しっとりと神社・仏閣めぐり',
             'シナリオなしの路線バスの旅',
             'モヤモヤする街を散策する',
             'ざわめく街の酒場を放浪する']
    # playリストからランダムに抽出
    tomorrow = random.choice(play)
    # 明日の予定ラベルにを表示
    response_area.configure(text=tomorrow)


#=================================================
# 画面を描画する関数
#=================================================
def run():
    # グローバル変数を使用するための記述
    global response_area

    # メインウィンドウを作成
    root = tk.Tk()
    # ウィンドウのタイトルを設定
    root.title('明日のデート : ')
    # フォントの用意
    font = ('Helevetica', 14)

    # キャンバスの作成
    canvas = tk.Canvas(
                root,                       # 親要素をメインウィンドウに設定
                width = 550,                # 幅を設定
                height = 200,               # 高さを設定
                relief=tk.RIDGE,            # 枠線を表示
                bd=2                        # 枠線の幅を設定
             )
    canvas.pack()                           # メインウィンドウ上に配置
    
    img = tk.PhotoImage(file = 'img1.gif')  # 表示するイメージを用意
    canvas.create_image(                    # キャンバス上にイメージを配置
        0,                                  # x座標
        0,                                  # y座標
        image = img,                        # 配置するイメージオブジェクトを指定
        anchor = tk.NW                      # 配置の起点となる位置を左上隅に指定
    )

    # 応答エリアを作成
    response_area = tk.Label(
                        root,               # 親要素をメインウィンドウに設定
                        width=50,           # 幅を設定
                        height=10,          # 高さを設定
                        bg='pink',          # 背景色を設定
                        font=font,          # フォントを設定
                        relief=tk.RIDGE,    # 枠線の種類を設定
                        bd=2                # 枠線の幅を設定
                        )
    response_area.pack()                    # メインウィンドウ上に配置

    # ボタンの作成
    button = tk.Button(
        root,                               # 親要素をメインウィンドウに設定
        font=font,                          # フォントを設定
        text='明日のデートはどーする？',    # ボタンに表示するテキスト
        command=wakuwaku                    # クリック時にwakuwaku()関数を呼ぶ
        )
    button.pack()                           # メインウィンドウ上に配置


    # メインループ
    root.mainloop()


#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    run()

