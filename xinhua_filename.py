#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-20
#文件名信息提取

import os
import pandas as pd
from collections import defaultdict

path='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2001501B-2002000B'
os.chdir(path)

filenames=os.listdir()
field=defaultdict(list)

for i in range(len(filenames)):
    filename=filenames[i]
    temp=filename.split('-')
    for j in range(len(temp)):
        if j==0:
            field['样本编号'].append(temp[j])
        elif j==1:
            field['姓名'].append(temp[j])
        elif j==len(temp)-1:
            field['NGS编号'].append(temp[j])
field=pd.DataFrame(field)
field.to_csv('infolist.csv',index=False,encoding='utf_8_sig')