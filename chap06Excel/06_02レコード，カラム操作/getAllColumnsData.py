import openpyxl, pprint
book  = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')          # Sheet1を取得

# 列データを順次、取り出す
for cells_obj in tuple(sheet.columns):
    for  cell_obj in cells_obj:
        print(cell_obj.value)
    print('--- 列のデータ終わり ---')             # 列の区切りを示す

