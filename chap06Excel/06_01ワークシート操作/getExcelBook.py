import openpyxl                                  # openpyxlをインポート

book = openpyxl.load_workbook('地形別面積.xlsx') # Excelブックを取得
print(type(book))                                # オブジェクトの種類を表示
      
