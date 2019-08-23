import openpyxl
import pprint

wb=openpyxl.load_workbook('censuspopdata.xlsx')
countydata={}

sheet=wb.active

for row in range(2,sheet.max_row+1):
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    countydata.setdefault(state,{})
    countydata[state].setdefault(county,{})
    countydata[state][county].setdefault('pop',0)
    countydata[state][county].setdefault('censustract',0)

    countydata[state][county]['pop']+=sheet['D'+str(row)].value
    countydata[state][county]['censustract']+=1

cd=open('censusdata.txt','w')
cd.write(pprint.pformat(countydata))

print('done')
