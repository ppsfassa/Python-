import openpyxl

# Excelブックを取得
book = openpyxl.load_workbook('地形別面積.xlsx')

# Sheet1を取得する
sheet = book.get_sheet_by_name('Sheet1')

# 1行目のタイトルを出力
print('A1セル:' + sheet['A1'].value)
print('B1セル:' + sheet['B1'].value)
print('C1セル:' + sheet['C1'].value)
print('D1セル:' + sheet['D1'].value)
print('E1セル:' + sheet['E1'].value)

# 2行目のデータを出力
print(sheet['A2'].value,
      sheet['B2'].value,
      sheet['C2'].value,
      sheet['D2'].value,
      sheet['E2'].value
      )
