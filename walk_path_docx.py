#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-29
#遍历检索所有的.docx和pdf，将搜索到的所有文件路径拆分成csv记录

import os
import shutil
import pandas as pd
from collections import defaultdict

'''遍历docx报告'''
rootpath='/mnt/e/NGS/二代测序第三REVIEW资料/'
os.chdir(rootpath)
paths_docx=pd.DataFrame()

for roots, dirs, files in os.walk(rootpath):
    filelists=os.listdir()
    for file in files:
        temp=defaultdict(list)
        if os.path.splitext(file)[1]=='.docx' and file.split('_')[0]=='NGS':
            path=os.path.join(roots,file).split('/')
            path_num=len(path)
            #temp['filename'].append(path[path_num-1])
            n=0
            for i in range(path_num-1,0,-1):
                n+=1
                temp[str(n)].append(path[i])
            temp=pd.DataFrame(temp)
            paths_docx=pd.concat([paths_docx,temp],axis=0)

paths_docx.to_csv('paths_docx.csv',index=False,encoding='utf_8_sig')   