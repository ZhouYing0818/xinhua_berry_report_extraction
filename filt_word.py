#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-25
#遍历所有子文件夹，将word报告复制出来

import os
import shutil
import pandas as pd
from collections import defaultdict
rootpath='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/'

copypath='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2000001B-2002000B_word报告'
os.chdir(copypath)

'''检索复制所有word报告'''
filepath=defaultdict(list)

for roots, dirs, files in os.walk(rootpath):
    filelists=os.listdir()
    for file in files:
        if os.path.splitext(file)[1]=='.docx' and file.split('_')[0]=='NGS':
            if file in filelists:
                continue
            else:
                path=os.path.join(roots,file)
                filepath['path'].append(path)
                shutil.copy(path,copypath)
                
'''获取当前文件夹数据三个信息'''
path='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2000001B-2002000B_word报告/'
os.chdir(path)

filenames=os.listdir()
field=defaultdict(list)

for i in range(len(filenames)):
    filename=filenames[i]
    temp=filename.split('-')
    field['NGS编号'].append(temp[0])
    field['样本编号'].append(temp[1])
    field['姓名'].append(temp[2])
    
field=pd.DataFrame(field)
field.to_csv('searchlist.csv',index=False,encoding='utf_8_sig')
filepath=pd.DataFrame(filepath)
filepath.to_csv('pathlist.csv',index=False,encoding='utf_8_sig')