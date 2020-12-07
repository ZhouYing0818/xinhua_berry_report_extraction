#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-20
#比对总表和文件名中信息

import os
import pandas as pd
from collections import defaultdict

path='/mnt/d/xinhua/2020.5.20_DATA/'
os.chdir(path)
filename='match_list.csv'

match_list=pd.read_csv(filename,header=0)
filed=pd.read_csv('infolist.csv',header=0)

'''判断NGS编号是否有不符合的,输出不符合的NGS号'''
infolist_NGS=filed.loc[:,'NGS编号'].dropna()
match_NGS=match_list.loc[:,'NGS编号'].dropna()

for i in range(len(infolist_NGS)):
    if infolist_NGS[i] in match_NGS.values:
        continue
    else:
        print('NGS not find:'+infolist_NGS[i])
        
'''判断姓名是否有不符合的'''
infolist_name=filed.loc[:,'姓名'].dropna()
match_name=match_list.loc[:,'姓名'].dropna()

for i in range(len(infolist_name)):
    if infolist_name[i] in match_name.values:
        continue
    else:
        print('Name not find:'+infolist_name[i])
        
'''判断样本编号是否有不符合的'''
infolist_sample=filed.loc[:,'样本编号'].dropna()
match_sample=match_list.loc[:,'样本编号'].dropna()

for i in range(len(infolist_sample)):
    if infolist_sample[i] in match_sample.values:
        continue
    else:
        print('Sample_num not find:'+infolist_sample[i])