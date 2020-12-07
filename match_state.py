#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-6-1
#统计符合和不符合标准正则表达式的文件

import os,re
import pandas as pd
from collections import defaultdict

match_file=defaultdict(list)
unmatch_file=defaultdict(list)

rootpath='/mnt/d/xinhua/'
os.chdir(rootpath)
NGS_paths=pd.read_csv('NGS_paths_docx.csv',header=0)
filenames=NGS_paths.iloc[:,0]

for i in range(len(filenames)):
    filename=filenames[i]
    m=re.match(r'(NGS_\d+(?:_[A-Z]+|.*?)_[A-Z]+).*?(\d\d+(?:[A-Z]+|\d)).*?([\u4E00-\u9FA5]{2,3})',filename)
    if m:
        match_file['filename'].append(filename)
    else:
        unmatch_file['filename'].append(filename)
        
match_file.to_csv('match_file.csv',index=False,encoding='utf_8_sig')
unmatch_file.to_csv('unmatch_file.csv',index=False,encoding='utf_8_sig')