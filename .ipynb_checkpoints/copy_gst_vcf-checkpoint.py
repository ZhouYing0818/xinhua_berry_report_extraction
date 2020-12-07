#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-7-8
#遍历所有子文件夹，将gst.vcf复制出来

import os
import shutil
import pandas as pd
from collections import defaultdict
rootpath='/data/MDP/二代测序第三REVIEW资料/'

copypath='/data/zhouying/NGS_gst/'
os.chdir(copypath)

'''检索复制所有word报告'''
#filepath=defaultdict(list)

for roots, dirs, files in os.walk(rootpath):
    filelists=os.listdir()
    for file in files:
        if os.path.splitext(file)[1]=='.vcf' and ('NGS' in file):
            if file in filelists:
                continue
            else:
                path=os.path.join(roots,file)
                #filepath['path'].append(path)
                shutil.copy(path,copypath)
