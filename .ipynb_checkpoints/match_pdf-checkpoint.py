#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-25
#检索总表中信息是否有对应的word报告

import os
import shutil
import pandas as pd
from collections import defaultdict

path='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2000001B-2002000B_pdf报告/'
os.chdir(path)

searchlist=pd.read_csv('searchlist.csv',header=0)
totallist=pd.read_csv('totallist.csv',header=0)
pathlist=pd.read_csv('pathlist.csv',header=0)

for i in range(len(totallist)):
    if isinstance(totallist.iloc[i,2], str):
        NGS=totallist.iloc[i,2].split('_')[0]+'_'+totallist.iloc[i,2].split('_')[1]
        ID=totallist.iloc[i,3]
        NAME=totallist.iloc[i,4]
    else:
        continue
    for j in range(len(searchlist)):
        ngs=searchlist.iloc[j,0]
        #Id=searchlist.iloc[j,1]
        #name=searchlist.iloc[j,2]
        if NGS==ngs:
            totallist.loc[i,'pdf_report']='YES'
        else:
            continue
    paths=''
    num=0
    for n in range(len(pathlist)):
        temp_path=pathlist.iloc[n,0].split('/')[6:]
        info=temp_path[len(temp_path)-1]
        temp_path='/'.join(temp_path)+'\n\n'
        if NGS in info:
            paths+=temp_path
            num+=1
        else:
            continue
            
    totallist.loc[i,'pdf_path']=paths
    if num>1:
        totallist.loc[i,'多个pdf']='YES'
    else:
        continue
totallist.to_csv('totallist_search.csv',index=False,encoding='utf_8_sig')