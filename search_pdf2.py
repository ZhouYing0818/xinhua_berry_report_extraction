import os
import shutil
import pandas as pd
from collections import defaultdict
import re
from colorama import Fore,Back,Style
path='/mnt/d/xinhua/pdf2/新华医院正式报告/'

copypath='/mnt/d/xinhua/pdf2/match_pdf/'
os.chdir(path)

'''检索复制所有pdf报告'''
dirslist=os.listdir()


for i in range(len(dirslist)):
    filename=dirslist[i]
    num=re.findall(r'GC\d+',filename)[0]
    for ID in Id:
        #print(str(i)+'. '+ID+' matching '+filename+'  working...')
        if ID ==num:
            filepath=path+dirslist[i]
            shutil.copy(filepath,copypath)
            print(Fore.RED+ID+' matched '+filename)
