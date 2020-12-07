#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-11-13
#PDF文件信息提取

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
    page2=list()
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
        elif i==2:
            layout2=device.get_result()
        #exec('layout'+str(i)+'=device.get_result()')
    page_num=i

    '''提取页面中的水平文本信息'''
    i=0
    for x in layout1:
        if(isinstance(x,LTTextBoxHorizontal)):
            i+=1
            results=x.get_text()
            if ngs in results:
                continue
            else:
                page1.append(results)

    i=0            
    for x in layout2:
        if(isinstance(x,LTTextBoxHorizontal)):
            i+=1
            results=x.get_text()
            if ngs in results:
                continue           
            else:
                page2.append(results)
    return page1,page2
     
def ND_extract(page1,page2,ngs):
    temp=defaultdict(list)
    temp['NGS编号'].append(ngs)
    #temp['报告名称'].append(page1[1])
    #temp['检测类型'].append(page1[2].split('：')[1])

    n=0
    flag=False
    tmp=''
    while n<len(page1):
        text=page1[n]
        n+=1
        if '检测结果' in text:
            flag=True
        elif '检测人' in text:
                flag=False
        if flag:
            tmp+=text
    temp['检测结果'].append(tmp)

    temp['基因'].append(page2[8])
    temp['突变位置'].append(page2[9])
    temp['外显子'].append(page2[10])
    temp['HGVS'].append(page2[11])
    temp['突变类型'].append(page2[12])
    temp['杂合性'].append(page2[13])
    temp['变异评级'].append(page2[14])
    temp['疾病及遗传方式'].append(page2[15])
    temp=pd.DataFrame(temp)
    return temp
    
def mutant_extract(page1,page2,ngs):
    temp=defaultdict(list)
    temp['NGS编号'].append(ngs)
    #temp['报告名称'].append(page1[1])
    #temp['检测类型'].append(page1[2].split('：')[1])

    n=0
    flag=False
    tmp=''
    while n<len(page1):
        text=page1[n]
        n+=1
        if '检测结果' in text:
            flag=True
        elif '检测人' in text:
            flag=False
        if flag:
            tmp+=text
    temp['检测结果'].append(tmp)

    row_num=0
    for m in page2:
        if 'exon' in m:
            row_num+=1

    temp['基因'].append('|'.join(page2[8:8+row_num]))
    temp['突变位置'].append('|'.join(page2[8+row_num:8+2*row_num]))
    temp['外显子'].append('|'.join(page2[8+2*row_num:8+3*row_num]))
    temp['HGVS'].append('|'.join(page2[8+3*row_num:8+4*row_num]))
    temp['突变类型'].append('|'.join(page2[8+4*row_num:8+5*row_num]))
    temp['杂合性'].append('|'.join(page2[8+5*row_num:8+6*row_num]))
    temp['变异评级'].append('|'.join(page2[8+6*row_num:8+7*row_num]))
    temp['疾病及遗传方式'].append('|'.join(page2[8+7*row_num:8+8*row_num]))
    temp=pd.DataFrame(temp)
    return temp

def negtive_report(page1,page2,ngs):
    temp=defaultdict(list)
    temp['NGS编号'].append(ngs)
    #temp['报告名称'].append(page1[1])
    #temp['检测类型'].append(page1[2].split('：')[1])

    n=0
    flag=False
    tmp=''
    while n<len(page1):
        text=page1[n]
        n+=1
        if '检测结果' in text:
            flag=True
        elif '检测人' in text:
                flag=False
        if flag:
            tmp+=text
    temp['检测结果'].append(tmp)

    temp=pd.DataFrame(temp)
    return temp


path='/data/zhouying/berry_report/新华医院'
os.chdir(path)

dirslist=os.listdir()
DataInfo=pd.DataFrame() #initial table

for m in range(402,len(dirslist)):
    #获取filename
    filename=dirslist[m]
    print(str(m)+'. '+filename+'  working...')
    ngs=re.findall(r'NGS_\d+|\dE\d+',filename)[0]
    page1,page2=extract_inform(filename)
    flag=False
    for line in page1:
        if "未检测到" in line:
            flag=True
            temp=negtive_report(page1,page2,ngs)
            break
    if (flag==False):
        if page2[8]=='ND':
            temp=ND_extract(page1,page2,ngs)
        else:
            temp=mutant_extract(page1,page2,ngs)
    DataInfo=pd.concat([DataInfo,temp],axis=0)
    DataInfo.to_csv('/data/zhouying/berry_report/PDF_extraction_DataInfo_4.csv',index=False,encoding='utf_8_sig')
