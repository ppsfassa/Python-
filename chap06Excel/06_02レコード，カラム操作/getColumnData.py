import openpyxl
book  = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')          # Sheet1を取得

t = tuple(sheet.columns)  # columnsで取得した列オブジェクトをタプルにする
for cell_obj in t[0]:     # 列オブジェクトのタプルから1列取り出す
    print(cell_obj.value)


