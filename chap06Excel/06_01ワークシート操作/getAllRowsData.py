import openpyxl
book  = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')          # Sheet1を取得

for cells_obj in tuple(sheet.rows):      # 1行のレコードを取り出す
    for  cell_obj in cells_obj:          # レコードからCellオブジェクトを取り出す
        print(cell_obj.value)
    print('--- 1行のレコード終わり ---') # 1行のレコードの区切りを示す
