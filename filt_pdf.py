#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-25
#遍历所有子文件夹，将pdf报告复制出来

import os
import shutil
import pandas as pd
from collections import defaultdict
rootpath='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/'

copypath='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2000001B-2002000B_pdf报告/'
os.chdir(copypath)

'''检索复制所有pdf报告'''
filepath=defaultdict(list)

for roots, dirs, files in os.walk(rootpath):
    filelists=os.listdir()
    for file in files:
        num=len(roots.split('/'))
        newname=roots.split('/')[num-2]+'*'+roots.split('/')[num-1]+'*'+file
        if os.path.splitext(file)[1]=='.pdf' and ('NGS' in file.split('_')) and ('1上海交通大学医学院附属新华医院' in file.split('_')):
            #print(newname)
            if file in filelists:
                continue
            else:
                path=os.path.join(roots,file)
                filepath['path'].append(path)
                shutil.copy(path,copypath)
                os.rename(file,newname)
                
'''获取当前文件夹数据三个信息'''
path='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2000001B-2002000B_pdf报告/'
os.chdir(path)

filenames=os.listdir()
field=defaultdict(list)

for i in range(len(filenames)):
    filename=filenames[i]
    temp=filename.split('*')[0].split('-')
    ngs=filename.split('*')[2].split('_')[2]+'_'+filename.split('*')[2].split('_')[3].split('.')[0]
    if 'NGS' in temp[len(temp)-1].split('_'):
        field['NGS编号'].append(ngs)
        #field['样本编号'].append(temp[0])
        #field['姓名'].append(temp[1])
    
field=pd.DataFrame(field)
field.to_csv('searchlist.csv',index=False,encoding='utf_8_sig')
filepath=pd.DataFrame(filepath)
filepath.to_csv('pathlist.csv',index=False,encoding='utf_8_sig')