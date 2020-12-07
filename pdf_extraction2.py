#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-8-19
#PDF文件信息提取2

import os 
import pandas as pd
import re
from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from collections import defaultdict

def extract_inform(filename):
    page1=list()
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
    i=0
    for page in doc.get_pages():
        i+=1
        interpreter.process_page(page)
        if i==1:
            layout1=device.get_result()
    i=0
    for x in layout1:
        if(isinstance(x,LTTextBoxHorizontal)):
            i+=1
            results=x.get_text()
            page1.append(results)
    return page1

path='/data/zhouying/berry_report/新华医院'
os.chdir(path)

dirslist=os.listdir()
DataInfo=pd.DataFrame() #initial table

for m in range(5):
    #获取filename
    filename=dirslist[m]
    print(str(m)+'. '+filename+'  working...')
    page1=extract_inform(filename)
    
    tmp=defaultdict(list)
    n=0
    for text in page1:
        n+=1
        if '实验编号' in text:
            ID=re.findall(r'GC\d+',text)
            tmp['实验编号'].append(ID)
        elif '检测结果' in text:
            temp=''
            for x in range(n,len(page1)):
                temp+=page1[x-1]
                if '结论描述'in page1[x-1]:
                    tmp['检测结果'].append(temp)
                    break
        elif '结论描述' in text:
            temp=''
            for x in range(n,len(page1)):
                temp+=page1[x]
                if 'CNV报告依据' in page1[x]:
                    break
            tmp['结论描述'].append(temp)
    tmp=pd.DataFrame(tmp)
    DataInfo=pd.concat([DataInfo,tmp],axis=0)
    DataInfo.to_csv('/data/zhouying/berry_report/DataInfo1.csv',index=False,encoding='utf_8_sig')
	
