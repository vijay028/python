#import openpyxl, pprint
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter

df = pd.read_excel('C:\Users\kulvi03\Google Drive\Python_Practice\data_files\\bugs_in_rally.xlsx', sheet_name='teamdata')
#writer = ExcelWriter('C:\Users\kulvi03\Google Drive\Python_Practice\data_files\\bugs_summary.xlsx')

workbook = xlsxwriter.Workbook('C:\Users\kulvi03\Google Drive\Python_Practice\data_files\\bugs_summary.xlsx')
worksheet = workbook.add_worksheet()

print ('opening the book..')

j=0
#print (df.columns)
for i in df.index:
    if (df['Priority'][i] == "1 - 1 - Resolve Immediately") :
        print (df['Formatted ID'][i] + "," + df['Name'][i])
        str_print = df['Formatted ID'][i] + "    " + df['Name'][i] + "    " + df['Owner'][i]
        worksheet.write_string(j,0,str_print)
        j=j+1
        #df.to_excel(writer,'Sheet2',index=True,na_rep=df['Formatted ID'][i] + " " + df['Name'][i])

workbook.close()
#writer.save()
