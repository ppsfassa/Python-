import openpyxl
from openpyxl.chart import BarChart, Series, Reference

book  = openpyxl.Workbook()   # ブックを生成
sheet = book.active           # アクティブなシートを取得

rows = [
    ('月', '商品A', '商品B'), # タイトル行と12行のレコードのタプルのリスト
    (1,  30, 35),
    (2,  10, 30),
    (3,  40, 60),
    (4,  50, 70),
    (5,  20, 10),
    (6,  30, 40),
    (7,  50, 30),
    (8,  65, 30),
    (9,  70, 30),
    (10, 50, 40),
    (11, 60, 50),
    (12, 65, 55),
]

for row in rows:               # 行数のぶんだけ繰り返す
    sheet.append(row)          # ワークシートに追加する

#### 列ごとに棒グラフを作成 ####
chart1 = BarChart()            # 棒グラフのオブジェクトを生成
chart1.type  = 'col'           # 列ごとにタテ棒を表示する
chart1.style = 10              # グラフのスタイルを設定
chart1.title = '年間売上'      # メインタイトル
chart1.y_axis.title = '売上高' # タテ軸のタイトル
chart1.x_axis.title = '月'     # ヨコ軸のタイトル

# データが入力されているセル範囲
data = Reference(sheet,        # 対象のワークシート
                 min_col=2,    # 開始列
                 min_row=1,    # 開始行
                 max_col=3,    # 終端列
                 max_row=13    # 終端行
                 )

# カテゴリデータのセル範囲
cats = Reference(sheet,        # 対象のワークシート
                 min_col=1,    # 開始列
                 min_row=2,    # 開始行
                 max_row=13)   # 終端行

# BarChartオブジェクトにデータを追加
chart1.add_data(data, titles_from_data=True)

# BarChartオブジェクトにカテゴリを追加
chart1.set_categories(cats)

# ワークシート上にグラフを追加
sheet.add_chart(chart1,        # 対象のワークシート
                'A16'          # グラフエリアの左上隅をA16セルに合わせる
                )

#### ヨコ型の棒グラフを作成 ####
from copy import deepcopy

chart2 = deepcopy(chart1)      # BarChartオブジェクトをコピー
chart2.type = 'bar'            # 列ごとにヨコ棒を表示する
chart2.style = 11              # グラフのスタイルを設定
sheet.add_chart(chart2,        # ワークシート上にグラフを追加
             'A32'             # グラフエリアの左上隅をD1セルに合わせる
             )

### 積み上げ型の棒グラフを作成 ####
chart3 = deepcopy(chart1)      # BarChartオブジェクトをコピー
chart3.type = 'col'            # タテ棒を表示する
chart3.style = 12              # グラフのスタイルを設定
chart3.grouping = 'stacked'    # データをそのまま積み上げる
chart3.overlap = 100           # 積み上げ棒をぴったり揃える
sheet.add_chart(chart3,        # ワークシート上にグラフを追加
             'I16'             # グラフエリアの左上隅をD1セルに合わせる
             )

### 積み上げ型のヨコ棒グラフを作成 ####
chart4 = deepcopy(chart1)          # BarChartオブジェクトをコピー
chart4.type = 'bar'                # ヨコ棒を表示する
chart4.style = 13                  # グラフのスタイルを設定
chart4.grouping ='percentStacked'  # データの比率で積み上げる
chart4.overlap = 100               # 積み上げ棒をぴったり揃える
sheet.add_chart(chart4,            # ワークシート上にグラフを追加
             'I32'                 # グラフエリアの左上隅をD1セルに合わせる
             )

book.save('barChart.xlsx')         # ブックを保存
