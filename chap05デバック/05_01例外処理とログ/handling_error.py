''' 四角形を描く関数

    pattern：パターン文字
    width  ：幅
    height ：高さ
'''
def draw_square(pattern, width, height):
    if len(pattern) != 1:
        raise Exception('patternは1文字であることが必要です')
    if width <= 2:
        raise Exception('widthは2より大きい値であることが必要です')
    if height <= 2:
        raise Exception('heightは2より大きい値であることが必要です')
    # 上辺を描画
    print(pattern * width)
    # 高さを描画
    for i in range(height - 2):
        print(pattern + (' ' * (width - 2)) + pattern)
    # 底辺を描画
    print(pattern * width)

# 繰り返しdraw_square()を実行
for pattern, w, h in (('#', 4, 4),  # 4×4の四角い枠
                      ('#', 1, 4),  # エラーになる値を設定
                      ('#', 4, 1),  # エラーになる値を設定
                      ('#', 40, 8)):# 40×7の四角い枠
    try:
        draw_square(pattern, w, h)  # draw_square()を実行
    except Exception as err:
        print('例外が発生しましたー> ' + str(err))
