import openpyxl, pprint
book  = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')          # Sheet1を取得

t = tuple(sheet.rows)     # columnsで取得したオブジェクトをタプルにする

for cell_obj in t[1]:     # レコードのタプルから1行取り出す
    print(cell_obj.value)

