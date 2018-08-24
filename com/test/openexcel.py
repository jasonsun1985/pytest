#-*-coding:utf-8 -*-
'''
Created on 2018年8月15日
操作EXCEL
@author: R07400
'''
import openpyxl

wb=openpyxl.load_workbook("D:\\temp\\员工成长计划-孙磊.xlsx")
print(wb.get_sheet_names())
str = wb.get_sheet_names()[0]
print(str)
sheet=wb.get_sheet_by_name(str)
print(sheet)