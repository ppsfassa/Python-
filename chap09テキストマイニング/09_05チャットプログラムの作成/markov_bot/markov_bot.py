import re
import random
from analyzer import *	                       # analyzerモジュールのインポート

class Markov:
    def make(self):
        """ マルコフ連鎖を利用して文章を作り出す
        """
        print('テキストを読み込んでいます...')
        filename = "bocchan.txt"               # ②
        with open(filename, 'r', encoding = 'utf_8') as f:
            text = f.read()                    # 全データをtextに格納

        text = re.sub('\n', '', text)          # 文末の改行文字を取り除く
        wordlist = parse(text)		       # 形態素の部分をリストとして取得

        markov = {}		               # マルコフ辞書の用意
        p1 = ''                                # プレフィックス用の変数
        p2 = ''                                # プレフィックス用の変数
        p3 = ''                                # プレフィックス用の変数

        for word in wordlist:                  # 形態素のリストから1つずつ取り出す
            if p1 and p2 and p3:    	       # p1、p2、p3に値が格納されているか
                if (p1, p2, p3) not in markov: # markovに(p1, p2, p3)キーが存在しない
                    markov[(p1, p2, p3)] = []  # なければキー：値のペアを追加
                markov[(p1, p2, p3)].append(word) # キーのリストにサフィックスを追加
            p1, p2, p3 = p2, p3, word          # 3つのプレフィックスの値を置き換える

        sentence = ''                          # 作り出した文章を保持する変数

    	# markovのキーをランダムに抽出し、プレフィックス1～3に代入
        p1, p2, p3  = random.choice(list(markov.keys()))
        count = 0                              # カウンター変数を初期化

        # マルコフ辞書を利用して文章を作り出す部分
        while count < len(wordlist):              # 単語リストの単語の数だけ繰り返す
            if ((p1, p2, p3) in markov) == True:  # キーが存在するかチェック
                tmp = random.choice(markov[(p1, p2, p3)]) # 文章にする単語を取得
                sentence += tmp                   # 取得した単語をsentenceに追加
            p1, p2, p3 = p2, p3, tmp              # プレフィックスの値を置き換える
            count += 1

        sentence = re.sub("^.+?。", "", sentence) # 最初に出現する(。)までを取り除く
        if re.search('.+。', sentence):           # 最後の句点(。)から先を取り除く
            sentence = re.search('.+。', sentence).group()
        sentence = re.sub("」", "", sentence)     # 閉じ括弧を削除
        sentence = re.sub("「", "", sentence)     # 開き括弧を削除
        sentence = re.sub("　", "", sentence)     # 全角スペースを削除
        return sentence                           # 生成した文章を戻り値として返す

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    markov = Markov()       # Markovクラスをインスタンス化
    text = markov.make()    # make()メソッドで生成された文章を取得
    ans = text.split('。')  # ③文末の。で切り分けてリストにする
    if '' in ans:           # ④空の要素を取り除く
        ans.remove('')
    print ('会話をはじめましょう。')
    while True:             # ⑤対話処理を実行
        message = input('>')
        if ans:
            # ansの中からランダムに1つの文章を抽出
            print(random.choice(ans))
