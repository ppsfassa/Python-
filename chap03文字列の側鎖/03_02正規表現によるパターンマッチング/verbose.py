import re

phone = re.compile(r'''(
    (0\d{0,3}|\(\d{0,3}\))  # 市外局番
    (\s|-)                  # 区切り
    (\d{1,4})               # 市内局番
    (\s|-)                  # 区切り
    (\d{3,4})               # 加入者番号
    )''', re.VERBOSE)
