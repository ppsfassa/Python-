import openpyxl
book  = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')          # Sheet1を取得

for row_obj in sheet['A2':'E7']:                  # 1行のレコードを取り出す
    for cell_obj in row_obj:                      # レコードからセルを取り出す
        print(cell_obj.coordinate,                # セル番地
              cell_obj.value                      # セルの値
              )
    print('--- 1行のレコード終わり ---')          # 1行のレコードの区切りを示す
    
