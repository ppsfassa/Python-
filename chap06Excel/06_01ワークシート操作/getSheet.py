import openpyxl

# Excelブックを取得
book = openpyxl.load_workbook('地形別面積.xlsx')

# Sheet1を取得する
sheet1 = book.get_sheet_by_name('Sheet1')
# sheet1のオブジェクトの種類を出力
print(type(sheet1))
# sheet1に格納されているシートのタイトルを出力
print(sheet1.title)
# アクティブなシートのタイトルを出力する
print(book.active.title)
