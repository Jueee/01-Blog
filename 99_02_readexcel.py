#读取excel使用(支持03)
import xlrd
#写入excel使用(支持03)
import xlwt3
#读取execel使用(支持07)
from openpyxl import Workbook
#写入excel使用(支持07)
from openpyxl import load_workbook


def showexcel(path):
    workbook=xlrd.open_workbook(path)
    sheets=workbook.sheet_names();
    #多个sheet时，采用下面的写法打印
    #for sname in sheets:
        #print(sname)
    worksheet=workbook.sheet_by_name(sheets[0])
    #nrows=worksheet.nrows
    #nclows=worksheet.ncols
    for i in range(0,worksheet.nrows):
        row=worksheet.row(i)

        for j in range(0,worksheet.ncols):
            print(worksheet.cell_value(i,j),"\t",end="")

        print()
read07path='C://Users//weiyq10580//Downloads//项目一览表.xls'
showexcel(read07path);