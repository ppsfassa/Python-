from janome.tokenizer import Tokenizer # janome.tokenizerをインポート
import re, pprint                      # reとpprintモジュールをインポート

''' 形態素解析を行う
    text   :解析対象の文章
    戻り値 :見出しと品詞のペアを格納した多重リスト
'''    
def analyze(text):                  # ①
    t = Tokenizer()                 # Tokenizerオブジェクトを生成
    tokens = t.tokenize(text)       # 形態素解析を実行
    result = []                     # ②形態素と品詞を格納するリスト
    
    for token in tokens:            # ③リストからTokenオブジェクトを1つずつ取り出す
        result.append(              # 形態素と品詞情報をリストにしてresultに追加
            [token.surface,         # 形態素を取得
             token.part_of_speech]) # 品詞情報を取得
    return(result)                  # 解析結果の多重リストを返す


#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':

    print('文章を入力')
    input = input()                  # 文章を取得
    pprint.pprint(analyze(input))    # 入力された文章を解析
