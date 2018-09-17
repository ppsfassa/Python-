import logging      # loggingモジュールのインポート

logging.basicConfig(# ログのレベルをDEBUG(詳細情報)にする
                    level=logging.DEBUG,
                    # ログの書式設定
                    # イベントの日付と時刻 - ログレベル - メッセージ
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# 最初のログを出力
logging.debug('プログラム開始')

# 階乗を計算する関数
def get_factorial(num):
    # ログ出力(処理の開始)
    logging.debug('factorial({})が実行されました'.format(num))
    fact = 1                    # 掛け算の初期値を設定
    for i in range(1, num + 1): # 1～num + 1になるまで繰り返す
        fact *= i               # factの値にiの値を掛けて再代入
        # ログ出力（iの値、factの値)
        logging.debug('i = {}, fact = {}'.format(i, fact))
    # ログ出力（処理終了）
    logging.debug('factorial({})終了'.format(num))
    return fact                 # 階乗した値を返す

# get_factorial()を呼び出して階乗を求める
print(get_factorial(5))

# ログ出力(プログラムの終了)
logging.debug('プログラム終了')
