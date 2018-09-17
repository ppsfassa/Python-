import openpyxl

book = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')         # Sheet1を取得
cel = sheet['A2']                                # セルA2を取得

# 列名、行番号、値を出力
print('列' + cel.column +       # 列名のみを取得
      ', 行' + str(cel.row) +   # 行番号のみを取得
      ' : ' + cel.value)        # セルの値を取得

# セル番地、値を出力
print('セル' + cel.coordinate + # 行列のセル番地を取得
      ' : ' + cel.value)        # セルの値を取得
