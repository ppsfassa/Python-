import re

# メールの正規表現
mail_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # ユーザー名
    @                  # @ 記号
    [a-zA-Z0-9.-]+     # ドメイン名
    (\.[a-zA-Z]{2,4})  # トップレベルドメイン
    )''', re.VERBOSE)

# テスト
str = '氏名:秀和太郎 住所:東京都中央区 メールアドレス:taro@shuwasystem.co.jp'
ml = mail_regex.search(str)
print(ml.group())
