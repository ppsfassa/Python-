import sys                                    # sysモジュールをインポート

while True:
    response = input("'exit'で終了します>")   # 入力値を取得
    if response == 'exit':                    # 入力値をチェック
        sys.exit()                            # 'exit'ならプログラム終了
    print(response + 'では終了できません')    # 'exit'でなければメッセージを表示
