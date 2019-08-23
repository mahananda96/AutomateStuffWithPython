import openpyxl

wb=openpyxl.load_workbook('freezeExample.xlsx')
sheet=wb.active

for row in range(2,sheet.max_row+1):
    if(sheet['A'+str(row)].value=='Celery'):
        sheet['B'+str(row)].value=1.19
    if(sheet['A'+str(row)].value=='Garlic'):
        sheet['B'+str(row)].value=3.07
    if(sheet['A'+str(row)].value=='Lemon'):
        sheet['B'+str(row)].value=1.27

wb.save('freezeExample2.xlsx')
