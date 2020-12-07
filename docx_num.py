#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-20
#统计子文件夹下的docx文件数目

import os
import pandas as pd
from collections import defaultdict
path='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2001501B-2002000B/'
os.chdir(path)

filenames=os.listdir()
filenames=filenames[:len(filenames)-1]
stat=defaultdict(list)

for i in range(len(filenames)):
    stat['filename'].append(filenames[i])
    n=0
    for roots,dirs,files in os.walk(filenames[i]):
        if roots != filenames[i]:
            break
        else:
            for file in files:
                if os.path.splitext(file)[1]=='.docx' and file.split('_')[0]=='NGS':
                    n+=1
    stat['num'].append(n)
stat=pd.DataFrame(stat)
stat.to_csv('docx_num.csv',index=False,encoding='utf_8_sig')