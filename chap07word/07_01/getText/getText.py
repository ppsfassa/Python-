import docx

def get_text(file):
    doc = docx.Document(file)
    all_text = []                  # テキストを保持するリスト
    for para in doc.paragraphs:    # Paragraphオブジェクトから要素を取り出す
        all_text.append(para.text) # テキストを取得してall_textに追加
    return '\n'.join(all_text)     # 改行を挟んで要素を連結し、戻り値として返す
    
