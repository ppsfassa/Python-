import openpyxl

# Excelブックを取得
book = openpyxl.load_workbook('地形別面積.xlsx')

# すべてのシート名を取得 
sheets_name = book.get_sheet_names()
print(sheets_name)

