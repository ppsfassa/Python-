import openpyxl, pprint
book  = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
sheet = book.get_sheet_by_name('Sheet1')          # Sheet1を取得

pprint.pprint((sheet['A2':'E7']))                 # A2～E7のCellオブジェクトを取得
