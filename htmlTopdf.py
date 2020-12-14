#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#流程
#1.下载wkhtmltopdf.exe: https://wkhtmltopdf.org/downloads.html
#2.安装: pip install pdfkit
#3.执行: htmlTopdf.py

# 导入库
import pdfkit


path_wkhtmltopdf = r'D:\\tools\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
htmlPath=input("请输入html地址:")
fileName=input("请输入pdf文件名:")
if(fileName.find('.pdf') == -1):
	fileName+='.pdf'
print("输入的html地址是:",htmlPath)
print("输入的pdf文件名是:",fileName)
pdfkit.from_url(htmlPath, fileName, configuration=config)


