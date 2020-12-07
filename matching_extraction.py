#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-7-7
#检索总表中信息是否有对应的word提取信息

import os
import shutil
import pandas as pd
from collections import defaultdict
import re

path='/mnt/d/xinhua/'
os.chdir(path)

searchlist=pd.read_csv('all_word.csv',header=0)
totallist=pd.read_csv('202起.csv',header=0)

for i in range(len(totallist)):
    if isinstance(totallist.iloc[i,0], str):
        NGS=str(totallist.iloc[i,0])
        ID=str(totallist.iloc[i,1])
        NAME=totallist.iloc[i,2]
    else:
        continue
    for j in range(len(searchlist)):
        if isinstance(searchlist.iloc[j,0], str):
            ngs=str(re.findall(r'(NGS_\d+_[A-Za-z]+_[A-Za-z])',searchlist.iloc[j,0]))
            Id=str(searchlist.iloc[j,1])
            #name=searchlist.iloc[j,2]
        if (ID in Id) or (NGS in ngs):
            totallist.loc[i,'word_report']='YES'
            searchlist.loc[j,'word_report']='YES'
        else:
            continue
totallist.to_csv('matching_202起.csv',index=False,encoding='utf_8_sig')
searchlist.to_csv('matched_202起.csv',index=False,encoding='utf_8_sig')