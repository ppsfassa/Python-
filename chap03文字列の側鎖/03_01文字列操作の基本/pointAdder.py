import pyperclip

# クリップボードのデータを取得
text = pyperclip.paste()
# 改行の位置で切り分ける
lines = text.split('\n')
# 切り分けた各行のデータに対して繰り返す
for i in range(len(lines)):
    # 先頭に*を追加する
    lines[i] = '# ' + lines[i]

#　改行を間に挟んで1つの文字列にまとめる
text = '\n'.join(lines)
# クリップボードにコピー
pyperclip.copy(text)
