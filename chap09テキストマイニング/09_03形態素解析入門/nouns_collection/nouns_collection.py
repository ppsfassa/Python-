from analyzer import *              # analyzerモジュールをインポート

file_name = ''                      # 辞書ファイル名を保持する変数

'''
辞書ファイルから名詞データを読み込む関数
    file   : 辞書ファイル名
    戻り値 : 辞書ファイルから抽出した名詞のリスト

'''
def read_dictionary(file):
    global file_name                # グローバル変数file_name
    file_name = file                # ファイル名をfile_nameに代入
    noun_lst = []                   # 辞書ファイルの名詞を保持するリスト
    pfile = open(                   # ファイルオープン
        file_name,                  # ファイルを指定
        'r',                        # 読み出し専用で開く
        encoding = 'utf_8'          # エンコード方式を指定
        )    
    p_lines = pfile.readlines()     # 1行ずつ読み込んでリストの要素にする
    pfile.close()                   # ファルクローズ
    
    for line in p_lines:            # p_linesから1行データを取り出す
        str = line.rstrip('\n')     # 1行のデータの末尾から改行文字を取り除く
        if (str!=''):               # 1行のデータが空文字ではない場合
            noun_lst.append(str)    # noun_lstに追加する

    return noun_lst                 # ファイルから抽出した名詞のリストを返す

'''
noun_lstの要素をまるごと辞書に書き込む関数
    noun_lst : 登録済みの名詞と新たに登録する名詞のリスト

'''
def save(noun_lst):
    nouns = []                      # 辞書ファイルに書き込むデータを保持するリスト
    for noun in noun_lst:           # noun_lstから名詞データを1つずつ取り出す
        nouns.append(noun + '\n')   # 末尾に改行を付加してnounsに追加する

    with open(                      # 辞書ファイルに書き込む
        file_name,                  # 辞書ファイルを指定
         'w',                       # 書き換えモードで開く
         encoding = 'utf_8'         # エンコード方式を指定
         ) as f:                    # イテレート可能なファイルオブジェクトとして取得する
        f.writelines(nouns)         # nounsの1行の名詞データをすべてファイルに書き込む

'''
名詞を学習する関数
    parts    : 形態素解析の結果のリスト
    noun_lst : 登録済みの名詞のリスト
'''
def study_noun(parts, noun_lst):    
    for word, part in parts:          # 多重リストの要素を2つのパラメーターに取り出す    
        if (keyword_check(part)):     # keyword_check()関数の戻り値がTrueの場合
            isNew = True              # フラグを立てておく           
            for element in noun_lst:  # リストnoun_lstを反復処理
                if(element == word):  # インプットされた名詞が既存の名詞とマッチする
                    isNew = False     # isNewをFalseにする
                    break             # ループを止める
            if isNew:                 # isNewがTrueである
                noun_lst.append(word) # リストnoun_lstに存在しない名詞なので追加する
    save(noun_lst)                    # save()でnoun_lstを辞書ファイルに書き込む

    
#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    # 辞書ファイルを読み込んで登録済みの名詞のリストを取得
    n_lst = read_dictionary('dictionary.txt')

    print('文章を入力')
    # 文章を取得
    input = input()
    # 入力された文章を解析
    result = analyze(input)            
    # 解析結果と登録済みの名詞のリストをを引数にして学習関数を呼ぶ
    study_noun(result, n_lst)       

