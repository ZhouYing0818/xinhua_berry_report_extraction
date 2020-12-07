#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-20
#PDF文件处理

import os 
from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

path='/mnt/d/xinhua/2001128B-杨一铭-全外显子组测序（NGS）-4422-P199-4-NGS_7560_BW_C/Analysis'
os.chdir(path)
filename='1上海交通大学医学院附属新华医院_9F7560_NGS_7560.pdf'

fp = open(filename,'rb')
#用文件对象创建一个PDF文档分析器
parser = PDFParser(fp)
#创建一个分析文档
doc = PDFDocument()

#连接分析器，与文档对象
parser.set_document(doc)
doc.set_parser(parser)

#提供初始化密码，如果没有密码，就创建一个空的字符串
doc.initialize()
#创建PDF，资源管理器，来共享资源
rsrcmgr = PDFResourceManager()
#创建一个PDF设备对象
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr,laparams=laparams)
#创建一个PDF解释其对象
interpreter = PDFPageInterpreter(rsrcmgr,device)

'''提取页面布局'''
for page in doc.get_pages():
    i+=1
    interpreter.process_page(page)
    exec('layout'+str(i)+'=device.get_result()')

'''提取页面中的水平文本信息'''
i=0    
for x in layout1:
    if(isinstance(x,LTTextBoxHorizontal)):
        i+=1
        results=x.get_text()
        if 'NGS_7560' in results:
            continue           
        else:
            print(str(i)+':'+results)