#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-5-20
#用样本编号，姓名，NGS编号信息格式化命名文件夹

import os
path='/mnt/d/xinhua/2020.5.20_DATA/2000001B-3000000B/2000001B-2000500B/'
os.chdir(path)

filenames=os.listdir()
filenames=filenames[:len(filenames)-1]

for i in range(len(filenames)):
    oldname=filenames[i]
    temp=oldname.split('-')
    newname=temp[0]+'-'+temp[1]+'-'+temp[len(temp)-1]
    os.rename(oldname,newname)