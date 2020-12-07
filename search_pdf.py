#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-6-8
#通过正则表达式检索所有路径下pdf报告

import os,re
import shutil
import pandas as pd
from collections import defaultdict

rootpath='/mnt/d/xinhua/'
os.chdir(rootpath)
totallist=pd.read_csv('P48_96.csv',header=0)
NGS_paths=pd.read_csv('NGS_paths_pdf.csv',header=0)
filenames=NGS_paths.iloc[:,0]

for i in range(len(totallist)):
    if isinstance(totallist.iloc[i,3], str):
        NGS='_'.join(totallist.iloc[i,3].split('_')[:2])
        #ID=totallist.iloc[i,4]
        #NAME=totallist.iloc[i,6]
    else:
        continue
    paths=''
    num=0
    for j in range(len(filenames)):
        filename=filenames[j]
        m=re.search(r'.*?(NGS_\d+)',filename)
        if m:
            ngs=m.group(1)
            #Id=m.group(2)
            #name=m.group(3)
        else:
            continue
            #ngs=re.findall(r'\w+',filename)[0]
            #Id='NAN'
            #name='NAN'
        if NGS==ngs:
            totallist.loc[i,'pdf_report']='YES'
            temp_path= '/'.join(NGS_paths.iloc[j,:6].dropna(axis=0))+'\n\n'
            paths+=temp_path
            num+=1
        else:
            continue
            
    totallist.loc[i,'pdf_path']=paths
    if num>1:
        totallist.loc[i,'多个pdf']='YES'
    else:
        continue
totallist.to_csv('P48_96_pdf.csv',index=False,encoding='utf_8_sig')